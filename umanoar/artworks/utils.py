from urllib.parse import urlparse, urljoin


def domain_from_url(url):
    r = urlparse(url)
    return r.scheme, r.netloc


def base_url(url):
    r = urlparse(url)
    return urljoin("{}://{}".format(r.scheme, r.netloc), r.path)
