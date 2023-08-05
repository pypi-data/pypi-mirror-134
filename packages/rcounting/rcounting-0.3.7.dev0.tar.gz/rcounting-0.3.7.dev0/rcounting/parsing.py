import re
from rcounting.models import RedditPost


def find_count_in_text(body, base=10, raise_exceptions=True):
    characters = "0123456789abcdefghijklmnopqrstuvwxyz"[:base]
    separators = "' , .*/"
    try:
        regex = (f"^[^{characters}]*"    # We strip characters from the start
                 rf"([{characters}{re.escape(separators)}]*)")  # We then take digits and separators
        count = re.findall(regex, body.lower())[0]
        # We remove any separators, and try to convert the remainder to an int.
        stripped_count = count.translate(str.maketrans("", "", separators))
        return int(stripped_count, base)
    except ValueError:
        if raise_exceptions:
            raise ValueError(f"Unable to extract count from comment body: {body}")
        else:
            return float("nan")


def find_urls_in_text(body):
    # reddit lets you link to comments and posts with just /comments/stuff,
    # so everything before that is optional. We only capture the bit after
    # r/counting/comments, since that's what has the information we are
    # interested in.
    url_regex = r"comments/([\w]+)?/?[^/]*/?([\w]*)"
    urls = re.findall(url_regex, body)
    return urls


def post_to_count(reddit_post, api=None):
    return find_count_in_text(RedditPost(reddit_post, api=api).body)


def post_to_urls(reddit_post, api=None):
    return find_urls_in_text(RedditPost(reddit_post, api=api).body)


def parse_markdown_links(body):
    regex = r'\[(.*?)\]\((.+?(?<!\\))\)'
    links = re.findall(regex, body)
    return links


def strip_markdown_links(body):
    regex = r'\[(.+?)\]\((.+?(?<!\\))\)'
    replacement = r'\1'
    return re.sub(regex, replacement, body)


def parse_directory_page(directory_page):
    paragraphs = directory_page.split("\n\n")
    regex = r"^.*\|.*\|.*$"
    tagged_results = []
    text = []
    for paragraph in paragraphs:
        lines = [line for line in paragraph.split("\n") if line]
        mask = all([bool(re.match(regex, line)) for line in lines])
        if not mask:
            text.append(paragraph)
        else:
            tagged_results.append(['text', '\n\n'.join(text)])
            text = []
            rows = [parse_row(row) for row in lines[2:]]
            tagged_results.append(['table', rows])
    if text:
        tagged_results.append(['text', '\n\n'.join(text)])
    return tagged_results


def parse_row(markdown_row):
    first, current, count = markdown_row.split("|")
    name, first_submission = parse_markdown_links(first)[0]
    name = name.strip()
    first_submission_id = first_submission.strip()[1:]
    title, link = parse_markdown_links(current)[0]
    title = title.strip()
    submission_id, comment_id = find_urls_in_text(link)[0]
    comment_id = None if not comment_id else comment_id
    count = count.strip()
    return name, first_submission_id, title, submission_id, comment_id, count


def parse_submission_title(title, regex):
    sections = [x.strip() for x in title.split("|")]
    match = re.match(regex, sections[-1])
    return [int(x) for x in match.groups()] if match is not None else match


def find_urls_in_submission(submission):
    # Get everything that looks like a url in the body of the post
    yield from find_urls_in_text(submission.selftext)
    # And then in every top-level comment
    for comment in submission.comments:
        yield from find_urls_in_text(comment.body)


def is_revived(title):
    regex = r'\(*reviv\w*\)*'
    return re.search(regex, title.lower())


def name_sort(name):
    title = name.translate(str.maketrans('', '', '\'"()^/*')).lower()
    return tuple(int(c) if c.isdigit() else c for c in re.split(r'(\d+)', title))


def normalise_title(title):
    title = title.translate(str.maketrans('[]', '()'))
    title = title.replace('|', '&#124;')
    revived = is_revived(title)
    if revived:
        start, end = revived.span()
        return title[:start] + '(Revival)' + title[end:]
    return title
