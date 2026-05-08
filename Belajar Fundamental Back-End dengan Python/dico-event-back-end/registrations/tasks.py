from celery import shared_task
from django.core.mail import EmailMultiAlternatives


@shared_task
def send_ticket_email(user_email, username, registration_id, event_name):
    subject = f'Konfirmasi Registrasi Tiket - Menunggu Pembayaran'

    # Plain text version
    text_content = f"""
Halo {username},

Terima kasih telah melakukan registrasi tiket di Dico Event.

Registrasi Anda berhasil dibuat dan saat ini sedang menunggu pembayaran.

Detail Registrasi:
- Event: {event_name}
- ID Registrasi: {registration_id}

Silakan lakukan pembayaran sesuai instruksi yang tersedia pada aplikasi/website.

Setelah pembayaran berhasil dikonfirmasi, tiket Anda akan diproses secara otomatis.

Terima kasih telah menggunakan Dico Event.

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
            
            <h2 style="color: #E50914; text-align: center;">
                Konfirmasi Registrasi Tiket
            </h2>

            <p>Halo <strong>{username}</strong>,</p>

            <p>
                Terima kasih telah melakukan registrasi tiket di 
                <strong>Dico Event</strong>.
            </p>

            <p>
                Registrasi Anda berhasil dibuat dan saat ini 
                <strong>sedang menunggu pembayaran</strong>.
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
            </div>

            <p>
                Silakan lakukan pembayaran sesuai instruksi yang tersedia 
                pada aplikasi/website.
            </p>

            <p>
                Setelah pembayaran berhasil dikonfirmasi, tiket Anda akan 
                diproses secara otomatis.
            </p>

            <br>

            <p>
                Terima kasih telah menggunakan 
                <strong>Dico Event</strong>.
            </p>

            <hr style="border: none; border-top: 1px solid #eeeeee; margin: 20px 0;">

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

    return f'Email sent to {user_email}'