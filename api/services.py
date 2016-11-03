# -*- coding: utf-8 -*-
"""`app.services` package.

Contains the external services for handling external functionality.
"""

import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

__all__ = ('mail_service', )


MAIL_TEMPLATE = """
<h1>Νέα αίτηση εγγραφής</h1><hr>
<strong>Όνομα</strong>: {name}<br>
<strong>Τηλέφωνο</strong>: {phone}<br>
<strong>Τάξη</strong>: {class}<br>
<strong>Σχολείο</strong>: {school}<br>
<strong>Διεύθυνση</strong>: {address}<br>
<hr>
"""


class ServiceError(Exception):
    """Raises when a service error occurs.
    """
    pass


def mail_service(from_email, context):
    """Send email through Gmail servers.

    Args:
        from_email (str): The Senders email.
        context: the email content

    Returns:
        True if email send is successful.

    Raises:
        ServiceError if anything occurs.

    Examples:
        >>> mail_context = {
        ...     'name': 'Παπαβασιλείου Βασίλης',
        ...     'class': 'Β Λυκείου',
        ...     'phone': '6971587292',
        ...     'school': '6ο ΓΕΛ Ιλίου',
        ...     'address': 'Γεωργίου Στράτου 15, Ίλιον'
        ... }
        >>> mail_service('student@ilion.gr', mail_context)
        True
    """

    mail = MIMEMultipart()
    mail['From'] = from_email
    mail['To'] = 'info@oroshmo.gr'
    mail['Subject'] = u'Εγγραφή ΟΡΟΣΗΜΟ - {}'.format(str(datetime.datetime.now()).split('.')[0])

    mail.attach(MIMEText(MAIL_TEMPLATE.format(**context), 'html'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as provider:
            provider.ehlo()
            provider.starttls()
            provider.login('vpapavasil@gmail.com', '#t9$T4k#!')
            provider.sendmail(
                from_email,
                'info@oroshmo.gr',
                mail.as_string()
            )
        return True

    except smtplib.SMTPException as error:
        raise ServiceError(error.args[0])


if __name__ == '__main__':

    import doctest
    doctest.testmod()
