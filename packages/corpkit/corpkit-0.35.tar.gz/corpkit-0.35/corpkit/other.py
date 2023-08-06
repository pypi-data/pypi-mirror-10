def quickview(results, n = 25):
    """view top n results of results"""
    import corpkit
    import pandas
    # bad hack to find out type of results
    if '.interrogation' in str(type(results)):
        option = results.query[1]
        try:
            results_branch = results.results
            resbranch = True
        except AttributeError:
            resbranch = False
    elif type(results) == pandas.core.frame.DataFrame:
        results_branch = results
        resbranch = True
        option = 'total' # not really used, just prevents error and prints n=
    elif type(results) == pandas.core.series.Series:
        resbranch = False
    if resbranch:
        for index, w in enumerate(list(results_branch)[:n]):
            fildex = '% 3d' % index
            if option == 'keywords':
                print '%s: %s (k=%d)' %(fildex, w, sum(i for i in list(results_branch[w])))
            elif option == '%':
                print '%s: %s' % (fildex, w)
            else:
                print '%s: %s (n=%d)' %(fildex, w, sum(i for i in list(results_branch[w])))
    else:
        print 'Totals:'
        print results

def concprinter(df, kind = 'string', n = 100):
    """print conc lines nicely, to string, latex or csv"""
    if n > len(df):
        n = len(df)
    if not kind.startswith('l') and kind.startswith('c') and kind.startswith('s'):
        raise ValueError('kind argument must start with "l" (latex), "c" (csv) or "s" (string).')
    import pandas as pd
    if type(n) == int:
        to_show = df.ix[range(n)]
    elif n is False:
        to_show = df
    elif n == 'all':
        to_show = df
    else:
        raise ValueError('n argument not recognised.')
    print ''
    if kind.startswith('s'):
        print to_show.to_string(header = False, formatters={'r':'{{:<{}s}}'.format(to_show['r'].str.len().max()).format})
    if kind.startswith('l'):
        print to_show.to_latex(header = False, formatters={'r':'{{:<{}s}}'.format(to_show['r'].str.len().max()).format})
    if kind.startswith('c'):
        print to_show.to_csv(sep = '\t', header = False, formatters={'r':'{{:<{}s}}'.format(to_show['r'].str.len().max()).format})
    print ''


def save_result(interrogation, savename, savedir = 'data/saved_interrogations'):
    """Save an interrogation as pickle to savedir"""
    from collections import namedtuple
    import pickle
    import os
    import pandas
    from time import localtime, strftime
    if not os.path.exists(savedir):
        os.makedirs(savedir)
    if not savename.endswith('.p'):
        savename = savename + '.p'
    fullpath = os.path.join(savedir, savename)
    if os.path.isfile(fullpath):
        raise ValueError("Save error: %s already exists in %s. Pick a new name." % (savename, savedir))
    
    # if it's just a table or series
    if type(interrogation) == pandas.core.frame.DataFrame or type(interrogation) == pandas.core.series.Series:
        temp_list = [interrogation]
    elif len(interrogation) == 2:
        temp_list = [interrogation.query, interrogation.totals]
    elif len(interrogation) == 3:
        temp_list = [interrogation.query, interrogation.results, interrogation.totals]
    elif len(interrogation) == 4:
        temp_list = [interrogation.query, interrogation.results, interrogation.totals, interrogation.table]
    else:
        try:
            temp_list = [interrogation.query, interrogation.results, interrogation.totals, interrogation.table]
        except:
            raise ValueError(' %s' % interrogation)
            
    f = open(fullpath, 'w')
    pickle.dump(temp_list, f)
    time = strftime("%H:%M:%S", localtime())
    print '\n %s: Data saved: %s\n' % (time, fullpath)
    f.close()

def load_result(savename, loaddir = 'data/saved_interrogations'):
    """Reloads a save_result as namedtuple"""
    import collections
    import pickle
    import os
    import pandas
    if not savename.endswith('.p'):
        savename = savename + '.p'
    unpickled = pickle.load(open(os.path.join(loaddir, savename), 'rb'))
    
    if type(unpickled) == pandas.core.frame.DataFrame or type(unpickled) == pandas.core.series.Series:
        output = unpickled
    elif len(unpickled) == 4:
        outputnames = collections.namedtuple('interrogation', ['query', 'results', 'totals', 'table'])
        output = outputnames(unpickled[0], unpickled[1], unpickled[2], unpickled[3])        
    elif len(unpickled) == 3:
        outputnames = collections.namedtuple('interrogation', ['query', 'results', 'totals'])
        output = outputnames(unpickled[0], unpickled[1], unpickled[2])
    elif len(unpickled) == 2:
        outputnames = collections.namedtuple('interrogation', ['query', 'totals'])
        output = outputnames(unpickled[0], unpickled[1])
    return output


def report_display():
    """Displays/downloads the risk report, depending on your browser settings"""
    class PDF(object):
        def __init__(self, pdf, size=(200,200)):
            self.pdf = pdf
            self.size = size
        def _repr_html_(self):
            return '<iframe src={0} width={1[0]} height={1[1]}></iframe>'.format(self.pdf, self.size)
        def _repr_latex_(self):
            return r'\includegraphics[width=1.0\textwidth]{{{0}}}'.format(self.pdf)
    return PDF('report/risk_report.pdf',size=(800,650))

def ipyconverter(inputfile, outextension):
    """ipyconverter converts ipynb files to various formats.

    This function calls a shell script, rather than using an API. 
    The first argument is the ipynb file. 
    The second argument is the file extension of the output format, which may be 'py', 'html', 'tex' or 'md'.

    Example usage: ipyconverter('infile.ipynb', 'tex')

    This creates a .tex file called infile-converted.tex
    """
    import os
    if outextension == 'py':
        outargument = '--to python ' # the trailing space is important!
    if outextension == 'tex':
        outargument = '--to latex '
    if outextension == 'html':
        outargument = '--to html '
    if outextension == 'md':
        outargument = '--to md '
    outbasename = os.path.splitext(inputfile)[0]
    output = outbasename + '-converted.' + outextension
    shellscript = 'ipython nbconvert ' + outargument + inputfile + ' --stdout > ' + output
    print "Shell command: " + shellscript
    os.system(shellscript)

def conv(inputfile, loadme = True):
    """A .py to .ipynb converter that relies on old code from IPython.

    You shouldn't use this: I only am while I'm on a deadline.
    """
    import os, sys
    import pycon.current as nbf
    import IPython
    outbasename = os.path.splitext(inputfile)[0]
    output = outbasename + '.ipynb'
    badname = outbasename + '.nbconvert.ipynb'
    print '\nConverting ' + inputfile + ' ---> ' + output + ' ...'
    nb = nbf.read(open(inputfile, 'r'), 'py')
    nbf.write(nb, open(output, 'w'), 'ipynb')
    os.system('ipython nbconvert --to=notebook --nbformat=4 %s' % output)
    os.system('mv %s %s' % (badname, output))
    if loadme:
        os.system('ipython notebook %s' % output)
    #nbnew = open(output, 'r')
    #IPython.nbformat.v4.convert.upgrade(nbnew, from_version=3, from_minor=0)
    print 'Done!\n'

def pytoipy(inputfile):
    """A .py to .ipynb converter.

    This function converts .py files to ipynb, relying on the IPython API. 
    Comments in the .py file can be used to delimit cells, headings, etc. For example:

    # <headingcell level=1>
    # A heading 
    # <markdowncell>
    # *This text is in markdown*
    # <codecell>
    # print 'hello'

    Example usage: pytoipy('filename.py')
    """
    import os
    import IPython.nbformat.current as nbf
    outbasename = os.path.splitext(inputfile)[0]
    output = outbasename + '.ipynb'
    print '\nConverting ' + inputfile + ' ---> ' + output + ' ...'
    nb = nbf.read(open(inputfile, 'r'), 'py')
    nbf.write(nb, open(output, 'w'), 'ipynb')
    print 'Done!\n'

def new_project(name):
    """make a new project in current directory"""
    import os
    import shutil
    import stat
    import platform
    import corpkit

    path_to_corpkit = os.path.dirname(corpkit.__file__)
    thepath, corpkitname = os.path.split(path_to_corpkit)
    
    # make project directory
    os.makedirs(name)
    # make other directories
    dirs_to_make = ['data', 'images']
    subdirs_to_make = ['dictionaries', 'saved_interrogations', 'corpus']
    for directory in dirs_to_make:
        os.makedirs(os.path.join(name, directory))
    for subdir in subdirs_to_make:
        os.makedirs(os.path.join(name, 'data', subdir))
    # copy the bnc dictionary to data/dictionaries
    shutil.copy(os.path.join(thepath, 'dictionaries', 'bnc.p'), os.path.join(name, 'data', 'dictionaries'))
    
    # make a blank ish notebook
    newnotebook_text = open(os.path.join(thepath, corpkitname, 'blanknotebook.ipynb')).read()
    fixed_text = newnotebook_text.replace('blanknotebook', str(name))
    with open(os.path.join(name, name + '.ipynb'), 'wb') as handle:
        handle.write(fixed_text)
        handle.close
    if platform.system() == 'Darwin':
        shtext = '#!/bin/bash\n\npath=$0\ncd ${path%%/*.*}\nipython notebook %s.ipynb\n' % name
        with open(os.path.join(name, 'launcher.sh'), 'wb') as handle:
            handle.write(shtext)
            handle.close
        # permissions for sh launcher
        st = os.stat(os.path.join(name, 'launcher.sh'))
        os.chmod(os.path.join(name, 'launcher.sh'), st.st_mode | 0111)
        print '\nNew project made: %s\nTo begin, either use:\n\n    ipython notebook %s.ipynb\n\nor run launcher.sh.\n\n' % (name, name)
    else:
        print '\nNew project made: %s\nTo begin, either use:\n\n    ipython notebook %s.ipynb\n\n' % (name, name)

def searchtree(tree, query, options = ['-t', '-o']):
    "Searches a tree with Tregex and returns matching terminals"
    import os
    from corpkit.other import tregex_engine
    from corpkit.tests import check_dit
    try:
        get_ipython().getoutput()
    except TypeError:
        have_ipython = True
    except NameError:
        import subprocess
        have_ipython = False
    on_cloud = check_dit()
    fo = open('tree.tmp',"w")
    fo.write(tree + '\n')
    fo.close()
    result = tregex_engine(query = query, check_query = True)
    result = tregex_engine(query = query, options = options, corpus = "tree.tmp")
    os.remove("tree.tmp")
    return result

def quicktree(sentence):
    """Parse a sentence and return a visual representation in IPython"""
    import os
    from nltk import Tree
    from nltk.draw.util import CanvasFrame
    from nltk.draw import TreeWidget
    try:
        from stat_parser import Parser
    except:
        raise ValueError('PyStatParser not found.')
    try:
        from IPython.display import display
        from IPython.display import Image
    except:
        pass
    try:
        get_ipython().getoutput()
    except TypeError:
        have_ipython = True
    except NameError:
        import subprocess
        have_ipython = False
    parser = Parser()
    parsed = parser.parse(sentence)
    cf = CanvasFrame()
    tc = TreeWidget(cf.canvas(),parsed)
    cf.add_widget(tc,10,10) # (10,10) offsets
    cf.print_to_file('tree.ps')
    cf.destroy()
    if have_ipython:
        tregex_command = 'convert tree.ps tree.png'
        result = get_ipython().getoutput(tregex_command)
    else:
        tregex_command = ["convert", "tree.ps", "tree.png"]
        result = subprocess.check_output(tregex_command)    
    os.remove("tree.ps")
    return Image(filename='tree.png')
    os.remove("tree.png")

def multiquery(corpus, query, sort_by = 'total'):
    """Creates a named tuple for a list of named queries to count.

    Pass in something like:

    [[u'NPs in corpus', r'NP'], [u'VPs in corpus', r'VP']]"""

    import collections
    import pandas
    import pandas as pd
    from corpkit.interrogator import interrogator
    from corpkit.editor import editor

    results = []
    for name, pattern in query:
        result = interrogator(corpus, 'count', pattern)
        result.totals.name = name # rename count
        results.append(result.totals)
    results = pd.concat(results, axis = 1)

    results = editor(results, sort_by = sort_by, print_info = False)
    
    return results


    # if nothing, the query's fine! 

def interroplot(path, query):
    from corpkit import interrogator, editor, plotter
    quickstart = interrogator(path, 't', query)
    edited = editor(quickstart.results, '%', quickstart.totals)
    plotter(str(path), edited.results)

def datareader(data, on_cloud = False):
    """
    Returns a string of plain text from a number of kinds of data.

    The kinds of data currently accepted are:

    path to corpus : all trees are flattened
    path to subcorpus : all trees are flattened
    conc() output (list of concordance lines)
    csv file generated with conc()
    a string of text
    """
    import os
    import pandas
    from corpkit.other import tregex_engine
    from corpkit.tests import check_dit
    try:
        get_ipython().getoutput()
    except TypeError:
        have_ipython = True
    except NameError:
        import subprocess
        have_ipython = False

    on_cloud = check_dit()
    
    # if unicode, make it a string
    if type(data) == unicode:
        if not os.path.isdir(data):
            if not os.path.isfile(data):
                good = data.encode('utf-8', errors = 'ignore')

    elif type(data) == str:
        # if it's a file, assume csv and get the big part
        if os.path.isfile(data):
            f = open(data)
            raw = f.read()
            # obsolete
            if data.endswith('csv'):
                bad, good = re.compile(r'Entire sentences \(n=[0-9]+\):').split(raw)
            else:
                good = raw
        # if it's a dir, flatten all trees
        elif os.path.isdir(data):
            is_trees = tregex_engine(corpus = data, check_for_trees = True)
            if is_trees:
                list_of_texts = tregex_engine(corpus = data,
                                  options = ['-o', '-t', '-w'], 
                                  query = r'__ !> __', 
                                  on_cloud = on_cloud)
            else:
                list_of_texts = []
                fs = [os.path.join(data, f) for f in os.listdir(data)]
                # do recursive if need
                if any(os.path.isdir(f) for f in fs):
                    recursive_files = []
                    for dirname, dirnames, filenames in os.walk(data):
                        for filename in filenames:
                            recursive_files.append(os.path.join(dirname, filename))
                    fs = recursive_files
                for f in fs:
                    raw = open(f).read()
                    list_of_texts.append(raw)
            good = '\n'.join(list_of_texts)
            try:
                good = good.encode('utf-8', errors = 'ignore')
            except:
                pass
        # if a string of text, just keyword that
        else:
            good = data.encode('utf-8', errors = 'ignore')
    # if conc results, turn into string...
    elif type(data) == pandas.core.frame.DataFrame:
        # if conc lines:
        try:
            if list(data.columns) == ['l', 'm', 'r']:
                conc_lines = True
            else:
                conc_lines = False
        except:
            conc_lines = False
        if conc_lines:
            good = '\n'.join([' '.join(list(data.ix[l])) for l in list(data.index)])
    else:
        raise ValueError('Input not recognised...')
    # if list of tokens...?
    
    return good

def tregex_engine(query = False, 
                  options = False, 
                  corpus = False, 
                  on_cloud = False, 
                  check_query = False,
                  check_for_trees = False):
    """This does a tregex query.
    query: tregex query
    options: list of tregex options
    corpus: place to search
    on_cloud: check_dit output
    check_query: just make sure query ok"""
    import subprocess 
    import re
    if on_cloud:
        tregex_command = ["sh", "tregex.sh"]
    else:
        tregex_command = ["tregex.sh"]

    if not query:
        query = 'NP'
    # if checking for trees, use the -T option
    if check_for_trees:
        options = ['-T']

    # append list of options to query    
    if options:
        [tregex_command.append(o) for o in options]
    if query:
        tregex_command.append(query)
    if corpus:
        tregex_command.append(corpus)
    # do query
    try:
        res = subprocess.check_output(tregex_command, stderr=subprocess.STDOUT).splitlines()
    # exception handling for regex error
    except Exception, e:
        res = str(e.output).split('\n')
    
    if check_query:
        # define error searches 
        tregex_error = re.compile(r'^Error parsing expression')
        regex_error = re.compile(r'^Exception in thread.*PatternSyntaxException')
        # if tregex error, give general error message
        if re.match(tregex_error, res[0]):
            tregex_error_output = "Error parsing Tregex expression. Check for balanced parentheses and boundary delimiters."
            raise ValueError(tregex_error_output) 
        
        # if regex error, try to help
        if re.match(regex_error, res[0]):
            info = res[0].split(':')
            index_of_error = re.findall(r'index [0-9]+', info[1])
            justnum = index_of_error[0].split('dex ')
            spaces = ' ' * int(justnum[1])
            remove_start = query.split('/', 1)
            remove_end = remove_start[1].split('/', -1)
            regex_error_output = 'Error parsing regex inside Tregex query:%s'\
            '. Best guess: \n%s\n%s^' % (str(info[1]), str(remove_end[0]), spaces)
            raise ValueError(regex_error_output)
        return True

    # remove errors and blank lines
    res = [s for s in res if not s.startswith('PennTreeReader:') and s]
    # find end of stderr
    regex = re.compile('(Reading trees from file|using default tree)')
    # remove stderr at start
    std_last_index = res.index(next(s for s in res if re.search(regex, s)))
    res = res[std_last_index + 1:]
    if check_for_trees:
        if res[0].startswith('1:Next tree read:'):
            return True
        else:
            return False
    # return if no matches
    if res[-1] == 'There were 0 matches in total.':
        return []
    # remove total
    res = res[:-1]
    return res
