# encoding: utf-8
import logging
import pyparsing
from pyparsing import *
import os
import html
import zml


def render(source, context={}):
    if source.endswith('.zml'):
        templatefile = source
        l = TemplateLookup(['.'])
        t = l.get_template(templatefile)
        out = t.render(context)
        return out
    else:
        out = Template()._rendercode(source, context)
        return out['_root']

zml.debugActive = False


def activateDebug(lfile):
    logging.basicConfig(
        filename=lfile,
        format="%(funcName)s (%(lineno)s) %(message)s",
        level=logging.DEBUG)
    zml.debugActive = True
    logfile = lfile


def debug(out):
    if zml.debugActive:
        logging.debug(out)


class TemplateLookup(object):

    def __init__(self, directories=None,
                 module_directory=None, input_encoding=None):
        self.directories = directories

    def get_template(self, template):
        for d in self.directories:
            abs_path = os.path.join(d, template)
            if os.path.exists(abs_path):
                return Template(abs_path, self)
        return None


class Template(object):

    def __init__(self, template=None, lookup=None, viewhelperdir=None):
        self.template = template
        self.lookup = lookup
        self.viewhelperdir = viewhelperdir
        self.context = dict()
        self.namespacemode = False
        self.namespaces = dict()

    def render(self, context=None, template=None, importmode=False):
        out = self._render(context, template, importmode=importmode)
        return out['_root']

    def intercode_line(self, code_indent_level, context_item, foo, comment=''):
        res = ' ' * 2 * code_indent_level
        res += "self.write('%s', '%s\\n') %s \n" % (
            context_item, foo, comment)
        return res

    def _render(self, context=None, template=None, indent_global='',
                importmode=False):

        if template is None:
            templatepath = self.template
        else:
            if self.lookup is None:
                templatepath = template
            else:
                templateobj = self.lookup.get_template(template)
                templatepath = templateobj.template
        with open(templatepath, 'r', encoding='utf-8') as f:
            zmlcode = f.read()
        return self._rendercode(zmlcode, context, importmode=importmode)

    def _rendercode(self, zmlcode=None, context=None,
                    indent_global='', importmode=False, code_indent_level=0):
        code_indent_last = code_indent_level * 2

        def escape_word(*args, **kwargs):
            return html.escape(args[2][0])
        context_item = '_root'
        code_indents = list()
        indents = list()
        lines = zmlcode.split('\n')[:-1]
        output = ''
        indent_last = ''
        tag_last = ''
        indents = list()
        code_indents = list()
        last_was_inline = False
        inherit_file = None
        lrev = list(reversed(lines))
        last_line = 0

        for i, line in enumerate(lrev):
            if len(line) == 0:
                last_line = len(lines)-i-1
                continue
            else:
                break
        lastnewline = False
        cil = ''
        inherit_file = None
        explicit_mode = False
        code_block_active = False
        word = Word(printables, excludeChars='{ }')
        lword = Word(printables+' ', excludeChars="{ } < >")
        descriptor = Word(printables+' ', excludeChars=": { } < >")
        attributekey = Word(printables, excludeChars=": = '")
        xword = Word(printables)
        nocolon = Word(printables, excludeChars=': # .')
        nomoustache = Word(printables, excludeChars='{ }')
        moustache_expression = Word(printables, excludeChars='{ }')
        moustacheline_expression = Word(printables, excludeChars='{ }')
        nomoustache.setWhitespaceChars('')
        quote = Suppress("'")
        uid = Suppress('#') + Word(printables, excludeChars='# : .')
        cls = Suppress('.') + Word(printables, excludeChars='. : #')
        classes = ZeroOrMore(cls)('classes')
        classes.setParseAction(lambda tokens: " ".join(tokens))
        id_classes = Optional(uid)('uid') + classes
        id_classes.setParseAction(lambda res: renderIdClasses(res))
        indentobj = ZeroOrMore(Literal(' '))
        indentobj.leaveWhitespace()
        colon = Optional(':')
        moustache = Suppress('{')
        moustache += moustache_expression('expression')
        moustache += Suppress('}')
        rawmoustache = Suppress('{')
        rawmoustache += moustache_expression('expression')
        rawmoustache += Suppress('}')
        descriptor = Word(printables, excludeChars='\. : - % *')
        isComponent = indentobj('indent') + descriptor('namespace') + \
            '-' + descriptor('component')

        def renderNormal(token):
            return '%s' % token

        def renderMoustache(token):
            return '\'+str('+token+')+\''

        def renderMoustacheLine(res):
            res.toString = 'str('+res.expression+')'
            return res

        def checkInlineColon(res):
            if len(res) == 0:
                res.has_colon = False
                return res
            res.has_colon = True
            if res.colon == '':
                res.has_colon = False
            return res

        def checkComponent(s):
            try:
                result = isComponent.parseString(s)
            except pyparsing.ParseException as x:
                return False
            return True

        def renderAttributes(res):
            if len(res) == 0:
                return ""
            return ' '.join(res)

        def renderAttributeValue(res):
            out = inline_attributevalue.parseString(res[0])
            return out

        def renderIdClasses(res):
            sep = ''
            clss = ''
            uid = ''
            if res.uid:
                uid = ' id="%s" ' % res.uid[0]
                sep = ' '
            else:
                uid = ''
            if res.classes:
                clss = ' class="%s" ' % res.classes
                sep = ' '
            else:
                clss = ''
            return uid+clss

        def serialize(*args, **kwargs):
            if len(args) == 0:
                args = "''"
            try:
                med = ["'%s'" % item for item in args[2]]
                out = "+' '+".join(med)
                out = out.replace("'", "\'")
                return out
            except Exception as e:
                debug('serialize Exception')
                debug(e)
                return ''

        def serialize_attributevalue(*args, **kwargs):
            try:
                if len(args[0]) > 0:
                    out = '+'.join(args[2])
                    return '"'+out+'"'
                else:
                    return ''
            except Exception as e:
                debug('serialize Exception')
                debug(e)
                return ''

        def renderWords(*args, **kwargs):
            items = [html.escape(item) for item in args[2]]
            return items

        def splitWords(*args, **kwargs):
            try:
                items = args[2].split()
                return items
            except Exception as e:
                debug('serialize Exception')
                debug(e)
                return ''

        def renderInlineTag(tokens):
            out = "<%s%s%s>%s</%s>" % (
                tokens.name, tokens.id_classes,
                tokens.attributes, tokens.ic, tokens.name)
            return out

        words = OneOrMore(lword('word'))('words')
#       words.leaveWhitespace()
        words_explicit = OneOrMore(lword('word'))('words')
        attributewords = OneOrMore(word('word'))('words')
#        words.setParseAction(renderWords)
        words_explicit.setParseAction(lambda tokens: " '+' ".join(tokens))
#       attributewords.setParseAction(lambda tokens: "'"+" ".join(tokens)+"'")
        moustache.setParseAction(lambda tokens: renderMoustache(tokens[0]))
        wordnoequal = Word(printables, excludeChars='=')
        wordnodash = Word(printables, excludeChars='- :')
        attribvalue = rawmoustache | Word(printables+' ', excludeChars="'")
        attrib = wordnoequal('key') + Suppress('=') + Suppress("'") + \
            attribvalue('value') + Suppress("'")
        attributevalue = moustache | Word(printables+' ', excludeChars="'")
#       attributevalue = moustache | lword
        attributevalue.setParseAction(lambda res: renderAttributeValue(res))
        attribute = attributekey + Literal('=')
        attribute += quote + attributevalue + quote
        attribute.setParseAction(lambda res: ''.join(res))
        attributes = ZeroOrMore(attribute)
        attributes.setParseAction(lambda res: renderAttributes(res))
        nomoustache.setParseAction(lambda tokens: renderNormal(tokens[0]))
        moustache_expression.setParseAction(
            lambda tokens: renderMoustache(tokens[0]))
        moustacheline_expression.setParseAction(
            lambda tokens: renderMoustacheLine(tokens))
        inlinetag = '<' + descriptor('name') + \
            id_classes('id_classes') + attributes('attributes') + \
            ': ' + ZeroOrMore(lword('ic')) + '>'
        inlinetag.setParseAction(renderInlineTag)
        inline_content = (
            Suppress(Optional("'")) +
            ZeroOrMore(
                moustache('moustache') | inlinetag('inline_tag') |
                words('words')) + Suppress(Optional("'"))) | (
            ZeroOrMore(
                moustache('moustache') |
                inlinetag('inline_tag') | nocolon('nocolon')))
        inline_content_explicit = ZeroOrMore(
            OneOrMore(moustache('moustache')) | words_explicit)
        inline_content.setParseAction(serialize)
        inline_content_explicit.setParseAction(serialize)
        inline_attributevalue = ZeroOrMore(
            OneOrMore(moustache('moustache')) | attributewords)
        indentobj.setParseAction(lambda tokens: "".join(tokens))
        inline_semantics = '<' + word('name') + ': ' + Optional("'") + \
            inline_content + Optional("'") + Optional(' ') + '>'
        inherit_line = Suppress('#') + Suppress('inherit')
        inherit_line += xword('templatefile')
        namespace_line = Suppress('#') + Suppress('namespace') + \
            Word(printables, excludeChars="=")('nsid')
        namespace_line += '=' + xword('namespace')
        import_line = Suppress('#') + Suppress('import')
        import_line += xword('module')
        moustache_line = indentobj('indent') + Suppress('{')
        moustache_line += moustacheline_expression('expression')
        moustache_line += Suppress('}')
        name = Word(printables, excludeChars='"  = : # .'+"'")
        inline_attributevalue.setParseAction(serialize_attributevalue)
        explicit_line = indentobj('indent')
        explicit_line += inline_content_explicit('inline_content')
        explicit_single_line = indentobj('indent') + Suppress('"')
        explicit_single_line += inline_content_explicit('inline_content')
        element = indentobj('indent') + Optional(name('name')) + \
            id_classes('id_classes')
        element += attributes('attributes') + colon('colon') + Optional(' ')
        element += inline_content('inline_content')
        viewhelper = indentobj('indent') + wordnodash('namespace') + '-' + \
            wordnodash('name') + id_classes('id_classes') + \
            Suppress(Optional(':'))
        viewhelper += ZeroOrMore(Group(attrib))('attribs')
        hasInlineColon = indentobj('indent') + Optional(name('name'))
        hasInlineColon += id_classes('id_classes') + attributes('attributes')
        hasInlineColon += Optional(colon('colon'))
        hasInlineColon += Optional(inline_content('inline_content'))
        hasInlineColon.setParseAction(lambda res: checkInlineColon(res))
        element_empty = indentobj('indent') + name('name')
        element_empty += id_classes('id_classes') + attributes('attributes')
        code_inline = indentobj('indent') + Suppress('%')
        code_inline += ZeroOrMore(Word(printables))('code')
        code_inlineblock = Suppress(Optional('<%')) + ZeroOrMore(
            Word(printables))('code') + Suppress(Optional('%>'))
        lnum = 0
        jump_to = 0
        last_was_text = False
        for i, line in enumerate(lines):
            is_text = False
            indstrs = [ind[0] for ind in indents]
            indstr = ','.join(indstrs)
            if jump_to > 0:
                if i < jump_to+1:
                    continue
                else:
                    jump_to = 0
            code_indent_level = int(code_indent_last / 2)
            newline = False
            if len(line.strip()) == 0:
                newline = True
            if line.strip().startswith('"'):
                res = explicit_single_line.parseString(line)
                ic = res.inline_content.replace("'''", "")
                ic = "'+%s+'" % (ic)
                output += self.intercode_line(
                    code_indent_level, context_item,
                    indent_global + res.indent + ic)
                last_was_inline = False
                continue
            if line.strip().startswith("'''") and \
               line.strip().endswith("'''") and \
               len(line.strip()) > 3:
                res = explicit_line.parseString(line.replace("'''", ""))
                ic = res.inline_content.replace("'''", "")
                ic = "'+%s+'" % (ic)
                output += self.intercode_line(
                    code_indent_level, context_item,
                    indent_global + res.indent + ic)
                last_was_inline = False
                continue
            if line.strip() == "'''":
                debug('explicit_mode')
                debug(line)
                explicit_mode = not explicit_mode
                continue
            indent_reduction = False
            if code_block_active:
                if line.strip().endswith('%>'):
                    code_block_active = False
                    if line.strip().startswith('<%'):
                        res = code_inlineblock.parseString(line)
                        output += res.code[0]
                else:
                    output += line + '\n'
            else:
                output += "# line: %s \n" % (line)
                if line.strip().startswith('#'):
                    if line.strip('#').strip().startswith('inherit'):
                        res = inherit_line.parseString(line)
                        inherit_file = res.templatefile
                    if line.strip('#').strip().startswith('namespace'):
                        res = namespace_line.parseString(line)
                        nsid = res.nsid
                        namespace = res.namespace
                        self.context['_namespace'] = nsid
                        self.namespacemode = True
                    if line.strip('#').strip().startswith('import'):
                        debug(line)
                        res = import_line.parseString(line)
                        m = res.module
                        (ns, components) = self.parseComponents(res.module)
                        self.namespaces[ns] = components
                elif line.strip().startswith('*'):
                    context_item = line[1:-1]
                    self.context[context_item] = ''
                elif line.strip().startswith('%'):
                    res = code_inline.parseString(line)
                    debug('code line')
                    code = " ".join(res.code)
                    output += "# code line \n"
                    output += "# len code indents: %s \n" % len(code_indents)
                    if len(code_indents) > 0:
                        code_indents_greater = [
                            ind for ind in code_indents
                            if len(ind[1]) >= len(res.indent)]
                        if len(code_indents_greater) > 0:
                            code_indents_greater.reverse()
                        for ind in code_indents_greater:
                            code_indents.pop(-1)
                            tag = ind[0]
                            if len(res.indent) <= len(ind[1]):
                                code_indent_level -= 1
                    code_indents.append([code, res.indent])
                    if code_indent_level < 0:
                        code_indent_level = 0
                    if len(res.indent) <= code_indent_last and \
                       len(code_indents) > 0:
                        code_indents_greater = [
                            ind for ind in code_indents
                            if len(ind[1]) >= len(res.indent)]
                        if len(code_indents_greater) > 0:
                            code_indents_greater.reverse()
                        for ind in code_indents_greater:
                            code_indents.pop(-1)
                            tag = ind[0]
                    if code_indent_level < 0:
                        code_indent_level = 0
                    if len(res.indent) <= len(indent_last) and \
                       len(indents) > 0:
                        indents_greater = [
                            ind for ind in indents
                            if len(ind[1]) >= len(res.indent)]
                        if len(indents_greater) > 0:
                            indents_greater.reverse()
                        for ind in indents_greater:
                            indents.pop(-1)
                            tag = ind[0]
                            indx = ind[1]
                            cindent = ind[2]
                            if last_was_inline:
                                indent_visible = ""
                                last_was_inline = False
                            else:
                                indent_visible = indx
                            output += "# tag: %s\n" % tag
                            output += self.intercode_line(
                                cindent, context_item, indent_global +
                                indent_visible + "</%s>" % tag)
                    # end close pending tags
                    output += "# code_indent_level: %s \n" % code_indent_level
                    output += ' ' * 2 * code_indent_level + code.strip() + '\n'
                    if code.strip().endswith(':'):
                        code_indent_level += 1
                elif line.strip().startswith('<%'):
                    code_block_active = True
                    if line.strip().endswith('%>'):
                        res = code_inlineblock.parseString(line)
                        output += res.code[0]
                        code_block_active = False
                elif line.strip().startswith('{'):
                    res = moustache_line.parseString(line)
                    if res.expression in self.context:
                        c = self.context[res.expression].split('\n')[:-1]
                        for lin in c:
                            output += ' ' * 2 * code_indent_level + \
                                "self.write('%s', '%s\\n')\n" % (
                                    context_item,
                                    indent_global +
                                    res.indent[(code_indent_level+1)*2:] + lin)
                    else:
                        try:
                            output += ' ' * 2 * code_indent_level + \
                                "self.write('" + context_item + "', " + \
                                indent_global + res.indent[code_indent_level*2:] + \
                                "str(" + res.expression + ")+'\\n')\n"
                        except Exception as e:
                            debug(e)
                elif len(line.strip()) == 0:
                    newline = True
                elif explicit_mode:
                    debug('explicit mode')
                    res = explicit_line.parseString(line)
                    ic = res.inline_content.replace("'''", "")
                    ic = "'+"+ic+"+'"
                    output += self.intercode_line(
                        code_indent_level, context_item,
                        indent_global + res.indent + ic)
                    last_was_inline = False
                elif not hasInlineColon.parseString(line).has_colon:
                    debug('no colon')
                    res = element_empty.parseString(line)
                    if '-' in res.name:
                        indentedrawcode = ''
                        unindentedrawcode = ''
                        resx = viewhelper.parseString(line)
                        for item in resx.attribs:
                            snipcode = item.key + '=' + item.value
                            indentedrawcode += ' ' * 2 * code_indent_level + \
                                snipcode + '\n'
                            unindentedrawcode += snipcode + '\n'
                        code_globals = globals()
                        code_locals = locals()
                        output += indentedrawcode
                        attr = res.attributes
                        c = dict()
                        ns = res.name.split('-')[0]
                        viewhelpercontext = {}
                        cc = self.namespaces[resx.namespace][resx.name]
                        componentcode = cc
                        compo = ''
                        for l in componentcode.split('\n'):
                            compo += ' ' * 2 * code_indent_level + l + '\n'
                        cr = self._rendercode(
                            compo,
                            {},
                            importmode=True,
                            code_indent_level=code_indent_level)
                        componentres = cr
                        output += componentres
                    else:
                        if len(res.indent) == 0:
                            context_item = '_root'
                            res.indent = ''
                        if len(code_indents) > 0:
                            code_indents_greater = [
                                ind for ind in code_indents
                                if len(ind[1]) >= len(res.indent)]
                            if len(code_indents_greater) > 0:
                                code_indents_greater.reverse()
                            for ind in code_indents_greater:
                                code_indents.pop(-1)
                                tag = ind[0]
                                if len(res.indent) < len(ind[1]):
                                    code_indent_level -= 1
                        if code_indent_level < 0:
                            code_indent_level = 0
                        if len(res.indent) <= len(indent_last) and \
                           len(indents) > 0:
                            indents_greater = [
                                ind for ind in indents
                                if len(ind[1]) >= len(res.indent)]
                            if len(indents_greater) > 0:
                                indents_greater.reverse()
                            for ind in indents_greater:
                                indents.pop(-1)
                                tag = ind[0]
                                cindent = ind[2]
                                code_indent_level = ind[2]
                                if last_was_inline:
                                    indent_visible = ""
                                    last_was_inline = False
                                else:
                                    indent_visible = ind[1]
                                output += self.intercode_line(
                                    cindent, context_item, indent_global +
                                    indent_visible + "</%s>" % tag)
                                if code_indent_level < 0:
                                    code_indent_level = 0
                        void_elements = [
                            'area', 'base', 'br', 'col', 'command',
                            'embed', 'hr', 'img', 'input', 'keygen',
                            'link', 'meta', 'param', 'source', 'track', 'wbr']
                        if res.name in void_elements:
                            closing_tag = ''
                        else:
                            closing_tag = '</%s>' % res.name
                        output += self.intercode_line(
                            code_indent_level, context_item, indent_global +
                            res.indent[code_indent_level*2:] + "<%s%s %s>" %
                            (res.name, res.id_classes, res.attributes) +
                            closing_tag)
                elif checkComponent(line):
                    indent_line = indentobj('indent') + Optional(name('name'))
                    res = indent_line.parseString(line)
                    # close greater indents before processing further
                    if len(res.indent) <= len(indent_last) and \
                       len(indents) > 0:
                        indents_greater = [
                            ind for ind in indents
                            if len(ind[1]) >= len(res.indent)]
                        if len(indents_greater) > 0:
                            indents_greater.reverse()
                        for ind in indents_greater:
                            allind = ind[1]
                            indents.pop(-1)
                            tag = ind[0]
                            cindent = ind[2]
                            output += "# d4 %s\n" % tag
                            if last_was_inline:
                                indent_visible = ""
                                last_was_inline = False
                            else:
                                indent_visible = ind[1]
                            output += self.intercode_line(
                                cindent, context_item, indent_global +
                                indent_visible + "</%s>" % tag, '# d2')
                            cil = cindent
                            code_indent_level = cil

                    remaining_lines = lines[i+1:]
                    component_indent = res.indent
                    childs = list()
                    n = 0
                    childs.append('')
                    l = 0
                    for lin in remaining_lines:
                        r = indent_line.parseString(lin)
                        indentlen = len(r.indent)
                        if indentlen <= len(res.indent):
                            break
                        if l > 0 and indentlen == len(res.indent) + 2:
                            childs.append('')
                            n += 1
                        childs[n] += lin + '\n'
                        l += 1
                    if l > 0:
                        jump_to = i+l
                    childitems = list()
                    for childcode in childs:
                        childres = render(childcode, context)
                        childitems.append(childres)
                    indentedrawcode = ''
                    unindentedrawcode = ''
                    resx = viewhelper.parseString(line)
                    for item in resx.attribs:
                        snipcode = item.key + '=' + item.value
                        indentedrawcode += ' ' * 2 * code_indent_level + \
                            snipcode + '\n'
                        unindentedrawcode += snipcode + '\n'
                    code_globals = globals()
                    code_locals = locals()
                    output += indentedrawcode
                    attr = res.attributes
                    c = dict()
                    ns = res.name.split('-')[0]
                    viewhelpercontext = {}
                    cc = self.namespaces[resx.namespace][resx.name]
                    componentcode = cc
                    compo = ''
                    for l in componentcode.split('\n'):
                        compo += ' ' * 2 * code_indent_level + l + '\n'
#                   _childs context item is deprecated and
#                   will be removed in the next release
                    cr = render(compo, {
                        '_children': childitems,
                        '_childs': childitems})
                    componentres = cr
                    output += 'self.write("""' + context_item + \
                        '""" , """ ' + componentres + '""")'
                elif hasInlineColon.parseString(line).has_colon:
                    debug('colon')
                    debug(line)
                    res = element.parseString(line)
                    if len(res.name) == 0:
                        is_text = True
                    cil = 0
                    rawline = line.strip()
                    allindent = len(res.indent)
                    codeindent = code_indent_last
                    contentindent = allindent-codeindent
                    if len(res.indent) == 0:
                        context_item = '_root'
                        res.indent = ''
                    code_indent_level_tmp = code_indent_level
                    # reduce code_indent_level
                    if len(code_indents) > 0:
                        code_indents_greater = [
                            ind for ind in code_indents
                            if len(ind[1]) >= len(res.indent)]
                        if len(code_indents_greater) > 0:
                            code_indents_greater.reverse()
                        for ind in code_indents_greater:
                            code_indents.pop(-1)
                            tag = ind[0]
                            if len(res.indent) < len(ind[1]):
                                code_indent_level -= 1
                    if code_indent_level < 0:
                        code_indent_level = 0
                    if len(res.indent) <= len(indent_last) and \
                       len(indents) > 0:
                        indents_greater = [
                            ind for ind in indents
                            if len(ind[1]) >= len(res.indent)]
                        if len(indents_greater) > 0:
                            indents_greater.reverse()
                        for ind in indents_greater:
                            allind = ind[1]
                            indents.pop(-1)
                            tag = ind[0]
                            cindent = ind[2]
                            output += "# d3 %s\n" % tag
                            if last_was_inline:
                                indent_visible = ""
                                last_was_inline = False
                            else:
                                indent_visible = ind[1]
                            output += self.intercode_line(
                                cindent, context_item, indent_global +
                                indent_visible + "</%s>" % tag, '# d2')
                            cil = cindent
                            code_indent_level = cil
                    if len(res.name) > 0:
                        indents.append([
                            res.name,
                            res.indent,
                            code_indent_level])
                    ic = res.inline_content.replace("'''", "")
                    if lastnewline:
                        if cil < code_indent_last:
                            output += ' ' * 2 * cil + \
                                "self.write('%s', '%s\\n') " + \
                                "# last newline1\n" % (
                                    context_item, indent_global +
                                    res.indent[(code_indent_level+1)*2:])
                        else:
                            output += ' ' * code_indent_last + \
                                "self.write('%s', '%s\\n') # last nl2\n" % (
                                    context_item, indent_global +
                                    res.indent[(code_indent_level+1)*2:])
                    if ic is None or ic == '':
                        ic = "''"
                    spacer = ''
                    if len(res.attributes) > 0:
                        spacer = ' '
                    if lastnewline and cil < code_indent_level:
                        if len(res.name) > 0:
                            output += ' ' * 2 * cil + \
                                "self.write('" + context_item + \
                                "', '%s%s<%s%s%s%s>'+%s) # d1a\n" % (
                                    indent_global,
                                    res.indent[code_indent_level*2:],
                                    res.name, res.id_classes, spacer,
                                    res.attributes, ic)
                        else:
                            output += ' ' * 2 * cil + \
                                "self.write('" + context_item + \
                                "', '%s%s'+%s) # d1a\n" % (
                                    indent_global,
                                    res.indent[code_indent_level*2:],
                                    ic)
                        if res.inline_content == '':
                            output += ' ' * 2 * cil + \
                                "self.write('" + context_item + \
                                "', '\\n')\n"
                    else:
                        if res.name == 'html':
                            output += "self.write('" + context_item + \
                                "', '<!DOCTYPE html>\\n')\n"
                        if len(res.name) > 0:
                            if last_was_text:
                                indent_vis = ''
                            else:
                                indent_vis = res.indent[code_indent_level*2:]
                            output += ' ' * 2 * code_indent_level + \
                                "self.write('" + context_item + \
                                "', '%s%s<%s%s%s%s>'+%s) # d1b1\n" % (
                                    indent_global,
                                    indent_vis,
                                    res.name, res.id_classes, spacer,
                                    res.attributes, ic)
                        else:
                            if last_was_text:
                                indent_vis = ''
                            else:
                                indent_vis = res.indent[code_indent_level*2:]
                            output += ' ' * 2 * code_indent_level + \
                                "self.write('" + context_item + \
                                "', '%s%s'+%s+'\\n') # d1b2\n" % (
                                    indent_global,
                                    indent_vis,
                                    ic)
                        if res.inline_content == '':
                            output += ' ' * 2 * code_indent_level + \
                                "self.write('" + context_item + "', '\\n')\n"
                    if len(res.inline_content) > 0:
                        last_was_inline = True
                    else:
                        last_was_inline = False
                    indent_last = res.indent
                    tag_last = res.name
                if "'''" in line:
                    explicit_mode = not explicit_mode
                last_was_text = is_text
            lastnewline = newline
            code_indent_last = code_indent_level * 2
            cil = code_indent_last
            for indent in indents:
                output += "# tag: %s indent: %s \n" % (
                    indent[0], len(indent[1]))
            lnum += 1

        if len(indents) > 0:
            indents.reverse()
        for ind in indents:
            tag = ind[0]
            if last_was_inline:
                indent_visible = ''
                last_was_inline = False
            else:
                indent_visible = ind[1]
            output += ' ' * 2 * ind[2] + \
                "self.write('" + context_item + "', '%s</%s>\\n')\n" % (
                    (indent_global + indent_visible)[ind[2]*2:], tag)
            if len(ind[1]) <= code_indent_last:
                code_indent_level -= 1
                code_indent_last = code_indent_level
        globals().update(context)
        debug(output)
        if importmode:
            return output
        else:
            exec(output)

        if inherit_file is not None:
            self.context = self._render(self.context, inherit_file)
        return self.context

    def set_templatedir(self, templatedir):
        self.templatedir = templatedir

    def set_viewhelperdir(self, viewhelperdir):
        self.viewhelperdir = viewhelperdir

    def write(self, context_item, code):
        if context_item not in self.context:
            self.context[context_item] = ''
        self.context[context_item] += code

    def parseComponents(self, template):
        namespace_line = Suppress('#') + Suppress('namespace') + \
            Word(printables, excludeChars="=")('nsid')
        namespace_line += '=' + Word(printables)('namespace')
        if template is None:
            templatepath = self.template
        else:
            if self.lookup is None:
                templatepath = template
            else:
                templateobj = self.lookup.get_template(template)
                templatepath = templateobj.template
        with open(templatepath, 'r', encoding='utf-8') as f:
            zmlcode = f.read()
            lines = zmlcode.split('\n')[:-1]
        components = dict()
        componentname = '_root'
        components[componentname] = list()
        namespace = '_default'
        for i, line in enumerate(lines):
            if line.strip().startswith('#'):
                if line.strip('#').strip().startswith('namespace'):
                    res = namespace_line.parseString(line)
                    nsid = res.nsid
                    namespace = res.nsid
            if line.startswith('*') and line.endswith(':'):
                componentname = line[1:-1]
                components[componentname] = list()
            else:
                components[componentname].append(line[2:])
        for component in components:
            components[component] = '\n'.join(components[component])
        return namespace, components
