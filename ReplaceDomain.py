

def replace_domain(email, old_domain, new_domain):
    if replace '@' + old_domain in email:
        index = email.index('@' + old_domain)
        ne_email = email[:index] +'@' + new_domain
        return new_email
    return email