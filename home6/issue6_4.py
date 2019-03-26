"""
Задание 4
Жду от вас письмо! (слайды 16-20). Воспользуйтесь менеджером контекста (with … as) (слайд 20)
(Не забудьте для себя понять код из официальной документации – слайд 19).
"""
import smtplib
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.starttls()
smtp_object.login('irinaursulenko@gmail.com', '******')
smtp_object.sendmail(from_addr="irinaurulenko@gmail.com",to_addrs="el.piankova@gmail.com", msg="Irina Ursulenko send message")
smtp_object.quit()
