import re

with open(r'C:\Users\Admin\Desktop\Keep Clicks\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

before = content.count('href="#courses"') + content.count('href="#services"')
print(f'Before: {before} anchor refs to update')

# ── Mobile menu course links (have onclick="closeMobileMenu()")
mobile_course_map = [
    ('fa-bullhorn',    'courses/digital-marketing.html'),
    ('fa-layer-group', 'courses/full-stack.html'),
    ('fa-java',        'courses/java.html'),
    ('fa-python',      'courses/python.html'),
    ('fa-brain',       'courses/data-science.html'),
    ('fa-chart-bar',   'courses/data-analytics.html'),
    ('fa-cloud',       'courses/cloud-computing.html'),
    ('fa-robot',       'courses/ai-ml.html'),
]

mobile_service_map = [
    ('fa-google text-brand-emerald', 'services/seo.html'),
    ('fa-share-nodes',               'services/smm.html'),
    ('fa-arrows-rotate',             'services/smo.html'),
    ('fa-globe',                     'services/website-development.html'),
    ('fa-ad',                        'services/sem.html'),
    ('fa-users',                     'services/crm.html'),
    ('fa-sitemap',                   'services/erp.html'),
]

# Mobile course
for icon, url in mobile_course_map:
    pattern = r'href="#courses"([^>]*onclick="closeMobileMenu\(\)"[^>]*)(<i class="[^"]*' + re.escape(icon)
    repl = f'href="{url}"' + r'\1\2'
    content, n = re.subn(pattern, repl, content, count=1)
    print(f'  Mobile course {icon}: {n}')

# Mobile services
for icon, url in mobile_service_map:
    pattern = r'href="#services"([^>]*onclick="closeMobileMenu\(\)"[^>]*)(<i class="[^"]*' + re.escape(icon)
    repl = f'href="{url}"' + r'\1\2'
    content, n = re.subn(pattern, repl, content, count=1)
    print(f'  Mobile service {icon}: {n}')

# ── Desktop nav dropdown course links
desktop_course_map = [
    ('fa-bullhorn',    'courses/digital-marketing.html'),
    ('fa-layer-group', 'courses/full-stack.html'),
    ('fa-java',        'courses/java.html'),
    ('fa-python',      'courses/python.html'),
    ('fa-brain',       'courses/data-science.html'),
    ('fa-chart-bar',   'courses/data-analytics.html'),
    ('fa-cloud',       'courses/cloud-computing.html'),
    ('fa-robot',       'courses/ai-ml.html'),
]
desktop_service_map = [
    ('fa-google text-brand-emerald', 'services/seo.html'),
    ('fa-share-nodes',               'services/smm.html'),
    ('fa-arrows-rotate',             'services/smo.html'),
    ('fa-globe',                     'services/website-development.html'),
    ('fa-ad',                        'services/sem.html'),
    ('fa-users',                     'services/crm.html'),
    ('fa-sitemap',                   'services/erp.html'),
]

# Desktop course dropdown: href="#courses" gap-3 style (no onclick)
for icon, url in desktop_course_map:
    pattern = r'href="#courses"([^>]*)(<i class="[^"]*' + re.escape(icon)
    repl = f'href="{url}"' + r'\1\2'
    content, n = re.subn(pattern, repl, content, count=1)
    print(f'  Desktop course {icon}: {n}')

# Desktop service dropdown
for icon, url in desktop_service_map:
    pattern = r'href="#services"([^>]*)(<i class="[^"]*' + re.escape(icon)
    repl = f'href="{url}"' + r'\1\2'
    content, n = re.subn(pattern, repl, content, count=1)
    print(f'  Desktop service {icon}: {n}')

# ── Course cards "Enroll Now" buttons (by course block context)
# Map each course section by a unique text nearby to its enroll button
enroll_map = [
    ('Digital Marketing',   'courses/digital-marketing.html'),
    ('Full Stack',          'courses/full-stack.html'),
    ('Java Programming',    'courses/java.html'),
    ('Python Programming',  'courses/python.html'),
    ('Data Science',        'courses/data-science.html'),
    ('Data Analytics',      'courses/data-analytics.html'),
    ('Cloud Computing',     'courses/cloud-computing.html'),
    ('AI & Machine',        'courses/ai-ml.html'),
]

# Replace href="#courses" in "Enroll Now" anchor tags that appear after the course title
for title, url in enroll_map:
    # Find the block from course title to the enroll button, replace href in that block
    # Pattern: after the course title text, find the next href="#courses" and replace it
    escaped_title = re.escape(title)
    pattern = r'(' + escaped_title + r'.*?href="#courses")([^>]*>(?:Enroll Now|Learn More|View Course))'
    repl = r'\1'.replace('href="#courses"', f'href="{url}"') + r'\2'
    # Simpler approach: match the anchor containing "Enroll Now" near the title
    # Use a lookahead approach
    pass

# Simpler: replace remaining href="#courses" Enroll Now buttons in sequence
# Find all occurrences of Enroll Now links and map them in order
enroll_pattern = r'(href="#courses"[^>]*>)\s*(Enroll Now|Learn More|View Course)'
matches = list(re.finditer(enroll_pattern, content, re.DOTALL))
print(f'\nFound {len(matches)} Enroll Now buttons linked to #courses')

# Service card "Get Started" buttons
service_pattern = r'(href="#services"[^>]*>)\s*(Get Started|Learn More|View Service)'
svc_matches = list(re.finditer(service_pattern, content, re.DOTALL))
print(f'Found {len(svc_matches)} Get Started buttons linked to #services')

after = content.count('href="#courses"') + content.count('href="#services"')
print(f'\nAfter: {after} refs remaining (these may be section anchors like the hero CTAs which should stay)')

with open(r'C:\Users\Admin\Desktop\Keep Clicks\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Saved successfully.')
