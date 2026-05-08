from celery import shared_task
from django.core.mail import EmailMultiAlternatives

@shared_task
def send_payment_success_email(
    user_email,
    username,
    registration_id,
    event_name
):
    subject = 'Pembayaran Berhasil - Tiket Anda Telah Dikonfirmasi'

    # Plain text version
    text_content = f"""
      Halo {username},

      Pembayaran Anda telah berhasil dikonfirmasi.

      Detail Tiket:
      - Event: {event_name}
      - ID Registrasi: {registration_id}

      Tiket Anda telah aktif dan siap digunakan.

      Silakan tunjukkan tiket atau bukti registrasi saat menghadiri event.

      Terima kasih telah menggunakan Dico Event.
      Kami tunggu kehadiran Anda!

      Salam,
      Tim Dico Event

      Pesan ini dikirim otomatis. Mohon tidak membalas email ini.
      """

    # HTML version
    html_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;">

        <div style="
            max-width: 600px;
            margin: auto;
            background-color: #ffffff;
            padding: 30px;
            border-radius: 10px;
            border: 1px solid #dddddd;
        ">

            <h2 style="color: #28a745; text-align: center;">
                Pembayaran Berhasil
            </h2>

            <p>Halo <strong>{username}</strong>,</p>

            <p>
                Pembayaran Anda telah berhasil dikonfirmasi.
            </p>

            <p>
                Tiket Anda sekarang sudah aktif dan siap digunakan.
            </p>

            <div style="
                background-color: #f8f8f8;
                padding: 15px;
                border-radius: 8px;
                margin: 20px 0;
            ">

                <p style="margin: 5px 0;">
                    <strong>Event:</strong> {event_name}
                </p>

                <p style="margin: 5px 0;">
                    <strong>ID Registrasi:</strong> {registration_id}
                </p>

                <p style="margin: 5px 0; color: #28a745;">
                    <strong>Status:</strong> Pembayaran Berhasil
                </p>

            </div>

            <p>
                Silakan tunjukkan tiket atau bukti registrasi saat menghadiri event.
            </p>

            <p>
                Terima kasih telah menggunakan 
                <strong>Dico Event</strong>.
            </p>

            <p>
                Kami tunggu kehadiran Anda!
            </p>

            <hr style="
                border: none;
                border-top: 1px solid #eeeeee;
                margin: 20px 0;
            ">

            <p style="
                font-size: 12px;
                color: #888888;
                text-align: center;
            ">
                Pesan ini dikirim otomatis. Mohon tidak membalas email ini.
            </p>

        </div>

    </body>
    </html>
    """

    email = EmailMultiAlternatives(
        subject,
        text_content,
        'no-reply@dicoevent.com',
        [user_email]
    )

    email.attach_alternative(html_content, "text/html")
    email.send()

    return f'Payment success email sent to {user_email}'

@shared_task
def send_event_reminder_email(
    user_email,
    username,
    event_name
):
    subject = f'Reminder Event - {event_name}'

    # Plain text version
    text_content = f"""
Halo {username},

Ini adalah pengingat bahwa event:

{event_name}

akan dimulai dalam 2 jam lagi.

Pastikan Anda datang tepat waktu dan menyiapkan tiket atau bukti registrasi Anda.

Sampai jumpa di event!

Salam,
Dico Event

Pesan ini dikirim otomatis. Mohon tidak membalas email ini.
"""

    # HTML version
    html_content = f"""
    <html>
    <body style="
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        padding: 20px;
    ">

        <div style="
            max-width: 600px;
            margin: auto;
            background-color: #ffffff;
            padding: 30px;
            border-radius: 10px;
            border: 1px solid #dddddd;
        ">

            <h2 style="
                color: #ff9800;
                text-align: center;
            ">
                Reminder Event
            </h2>

            <p>
                Halo <strong>{username}</strong>,
            </p>

            <p>
                Ini adalah pengingat bahwa event berikut akan dimulai dalam
                <strong>2 jam lagi</strong>.
            </p>

            <div style="
                background-color: #f8f8f8;
                padding: 15px;
                border-radius: 8px;
                margin: 20px 0;
            ">

                <p style="margin: 5px 0;">
                    <strong>Event:</strong> {event_name}
                </p>

                <p style="
                    margin: 5px 0;
                    color: #ff9800;
                ">
                    <strong>Status:</strong> Akan segera dimulai
                </p>

            </div>

            <p>
                Pastikan Anda datang tepat waktu dan menyiapkan tiket atau
                bukti registrasi Anda.
            </p>

            <p>
                Kami tunggu kehadiran Anda.
            </p>

            <br>

            <p>
                Salam,<br>
                <strong>Dico Event</strong>
            </p>

            <hr style="
                border: none;
                border-top: 1px solid #eeeeee;
                margin: 20px 0;
            ">

            <p style="
                font-size: 12px;
                color: #888888;
                text-align: center;
            ">
                Pesan ini dikirim otomatis. Mohon tidak membalas email ini.
            </p>

        </div>

    </body>
    </html>
    """

    email = EmailMultiAlternatives(
        subject,
        text_content,
        'no-reply@dicoevent.com',
        [user_email]
    )

    email.attach_alternative(html_content, "text/html")

    email.send()

    return f'Reminder email sent to {user_email}'