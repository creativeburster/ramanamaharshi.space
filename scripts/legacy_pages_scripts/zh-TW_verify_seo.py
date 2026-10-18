import glob, re, os

os.chdir(r'C:\Users\willp\WorkBuddy\20260410104230\pages')

check = [
    'index.html',
    'books/index.html',
    'books/be-as-you-are-ch1.html',
    'books/gems-ch4.html',
    'concepts/self-enquiry.html',
    'qa/qa-1.html',
    'qa/qa-9.html',
    'persons/ramana.html',
    'graph.html',
]
for fp in check:
    if os.path.exists(fp):
        with open(fp, encoding='utf-8') as f:
            content = f.read()
        m_title = re.search(r'<title>(.*?)</title>', content)
        m_robot = re.search(r'name="robots" content="(.*?)"', content)
        m_canon = re.search(r'rel="canonical" href="(.*?)"', content)
        print(fp + ':')
        print('  title: ' + str(m_title.group(1) if m_title else None))
        print('  robots: ' + str(m_robot.group(1) if m_robot else None))
        print('  canonical: ' + str(m_canon.group(1) if m_canon else None))
