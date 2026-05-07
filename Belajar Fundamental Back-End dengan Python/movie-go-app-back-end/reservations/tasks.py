from celery import shared_task
from django.core.mail import EmailMultiAlternatives
 
@shared_task
def send_ticket_email(user_email, username, reservation_id):
    subject = f'Konfirmasi Pemesanan Tiket di Movie Go'
 
    # Plain text version (fallback for email clients that don't support HTML)
    text_content = f"""Halo {username},
 
    Terima kasih telah memesan tiket di Movie Go!
 
    Berikut adalah detail pemesanan tiket Anda:
 
    ID Pemesanan: {reservation_id}
 
    Silakan datang ke bioskop 30 menit sebelum film dimulai untuk melakukan pembayaran.
 
    Kami tunggu kedatangan Anda di Cinema, selamat menonton!
 
    Terima kasih,
    Tim Movie Go
 
    Pesan ini dikirim secara otomatis. Mohon tidak membalas pesan ini.
    """
 
    # HTML formatted version
    html_content = f"""
        <html>
        <body style="font-family: Arial, sans-serif; color: #333;">
            <div style="max-width: 600px; margin: auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px;">
                <h2 style="color: #E50914; text-align: center;">Konfirmasi Pemesanan Tiket</h2>
                <p>Halo <strong>{username}</strong>,</p>
                <p>Terima kasih telah memesan tiket di <strong>Movie Go</strong>!</p>
                <p><strong>Detail Pemesanan Tiket Anda:</strong></p>
                <p style="background-color: #f8f8f8; padding: 10px; border-radius: 5px;">
                    <strong>ID Pemesanan:</strong> {reservation_id}
                </p>
                <p>Silakan datang ke bioskop <strong>30 menit sebelum film dimulai</strong> untuk melakukan pembayaran.</p>
                <p>Kami tunggu kedatangan Anda di Cinema, selamat menonton! ????</p>
                <br>
                <p style="font-size: 12px; color: #777; text-align: center;">
                    Pesan ini dikirim secara otomatis. Mohon tidak membalas pesan ini.
                </p>
                <p style="font-size: 12px; color: #777; text-align: center;">
                    <strong>Movie Go Team</strong>
                </p>
            </div>
        </body>
        </html>
        """
 
    email = EmailMultiAlternatives(subject, text_content, 'no-reply@movieticket.com', [user_email])
    email.attach_alternative(html_content, "text/html")
    email.send()
    return f'Email sent to {user_email}'