import re
import dns.resolver


class NoSpfRecordException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class SpfRecord(object):

    def __init__(self):
        self.version = None
        self.record = None
        self.mechanisms = None
        self.all_string = None

    def get_redirected_record(self):
        redirect_domain = self.get_redirect_domain()
        if redirect_domain is not None:
            return get_spf_string_for_domain(redirect_domain)

    def get_redirect_domain(self):
        redirect_domain = None
        for mechanism in self.mechanisms:
            redirect_mechanism = re.match('redirect=(.*)', mechanism)
            if redirect_mechanism is not None:
                redirect_domain = redirect_mechanism.group(1)
        return redirect_domain

    @staticmethod
    def from_spf_string(spf_string):
        spf_record = SpfRecord()
        spf_record.record = spf_string
        spf_record.mechanisms = _extract_mechanisms(spf_string)
        spf_record.version = _extract_version(spf_string)
        spf_record.all_string = _extract_all_mechanism(spf_record.mechanisms)
        return spf_record

    @staticmethod
    def from_domain(domain):
        return SpfRecord.from_spf_string(get_spf_string_for_domain(domain))


def _extract_version(spf_string):
    version_pattern = "^v=(spf.)"
    version_match = re.match(version_pattern, spf_string)
    if version_match is not None:
        return version_match.group(1)
    else:
        return None


def _extract_all_mechanism(mechanisms):
    all_mechanism = None
    for mechanism in mechanisms:
        if re.match(".all", mechanism):
            all_mechanism = mechanism
    return all_mechanism


def _find_unique_mechanisms(initial_mechanisms, redirected_mechanisms):
    return [x for x in redirected_mechanisms if x not in initial_mechanisms]


def _extract_mechanisms(spf_string):
    spf_mechanism_pattern = ("(?:((?:\+|-|~)?(?:a|mx|ptr|include"
                             "|ip4|ip6|exists|redirect|exp|all)"
                             "(?:(?::|/)?(?:\S*))?) ?)")
    spf_mechanisms = re.findall(spf_mechanism_pattern, spf_string)

    return spf_mechanisms


def _match_spf_record(txt_record):
    spf_pattern = re.compile('^"(v=spf.*)"')
    potential_spf_match = spf_pattern.match(str(txt_record))
    return potential_spf_match


def _find_record_from_answers(txt_records):
    spf_record = None
    for record in txt_records:
        potential_match = _match_spf_record(record)
        if potential_match is not None:
            spf_record = potential_match.group(1)
    return spf_record


def get_spf_string_for_domain(domain):
    try:
        txt_records = dns.resolver.query(domain, "TXT")
        return _find_record_from_answers(txt_records)
    except dns.resolver.NoAnswer:
        return None
