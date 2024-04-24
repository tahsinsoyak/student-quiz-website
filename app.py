from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

highest_score = 0

class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100), nullable=False)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.Text, nullable=False)
    answer = db.Column(db.String(100), nullable=False)
    choices = db.Column(db.String(300), nullable=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'), nullable=False)

with app.app_context():
    # Veritabanını oluştur
    db.create_all()

    # Python'da AI geliştirme sınavı
    exam1 = Exam.query.filter_by(topic="Python'da AI geliştirme").first()
    if not exam1:
        exam1 = Exam(topic="Python'da AI geliştirme")
        db.session.add(exam1)
        db.session.commit()

        question1 = Question(question_text="Karar verme için kullanılan aşağıdaki yapılardan hangisi bir AI tekniğidir?",
                             answer="Makine Öğrenimi",
                             choices="Makine Öğrenimi|Veri Yapıları|Algoritma Analizi|Veritabanı Yönetimi",
                             exam_id=exam1.id)
        db.session.add(question1)

        question2 = Question(question_text="AI bağlamında SVM'nin açılımı nedir?",
                             answer="Destek Vektör Makinesi",
                             choices="Basit Vektör Makinesi|Destek Vektör Makinesi|Sıralı Vektör Modeli|Senkron Değişim Yöntemi",
                             exam_id=exam1.id)
        db.session.add(question2)

        question3 = Question(question_text="Python'da derin öğrenme görevlerinde genellikle hangi kütüphane kullanılır?",
                             answer="TensorFlow",
                             choices="SciKit-Learn|TensorFlow|Pandas|Matplotlib",
                             exam_id=exam1.id)
        db.session.add(question3)

        db.session.commit()

    # Bilgisayar görüşü sınavı
    exam2 = Exam.query.filter_by(topic="Bilgisayar görüşü").first()
    if not exam2:
        exam2 = Exam(topic="Bilgisayar görüşü")
        db.session.add(exam2)
        db.session.commit()

        question4 = Question(question_text="Görüntü bölütleme ne amaçla kullanılır?",
                             answer="Bir görüntüyü birden çok segmente ayırmak",
                             choices="Bir görüntüdeki nesneleri algılamak|Bir görüntüdeki renkleri tanımlamak|Bir görüntüyü birden çok segmente ayırmak|Bir görüntüyü bulanıklaştırmak",
                             exam_id=exam2.id)
        db.session.add(question4)

        question5 = Question(question_text="Görüntülerde nesne tespiti için genellikle hangi algoritma kullanılır?",
                             answer="YOLO (You Only Look Once)",
                             choices="SVM (Destek Vektör Makinesi)|K-ortalama kümeleme|YOLO (You Only Look Once)|Rastgele Orman",
                             exam_id=exam2.id)
        db.session.add(question5)

        question6 = Question(question_text="Görüntü işleme bağlamında CNN'nin açılımı nedir?",
                             answer="Evrişimli Sinir Ağı",
                             choices="Eş zamanlı Sinir Ağı|Evrişimli Sinir Ağı|Sürekli Sinir Ağı|Korelasyonlu Sinir Ağı",
                             exam_id=exam2.id)
        db.session.add(question6)

        db.session.commit()

    # NLP (Nöro-dilbilim) sınavı
    exam3 = Exam.query.filter_by(topic="NLP (Nöro-dilbilim)").first()
    if not exam3:
        exam3 = Exam(topic="NLP (Nöro-dilbilim)")
        db.session.add(exam3)
        db.session.commit()

        question7 = Question(question_text="NLP'de POS etiketleme ne anlama gelir?",
                             answer="Sözcük türü etiketleme",
                             choices="Konumlandırma Çıkış Sistemi etiketleme|Sözcük türü etiketleme|Birincil Nesne Sözdizimi|Güçlü Nesne Yapısı",
                             exam_id=exam3.id)
        db.session.add(question7)

        question8 = Question(question_text="Aşağıdakilerden hangisi NLP'de yaygın bir görevdir?",
                             answer="Adlandırılmış Varlık Tanıma",
                             choices="Görüntü Bölütleme|Adlandırılmış Varlık Tanıma|Konuşma Sentezi|Yüz Tanıma",
                             exam_id=exam3.id)
        db.session.add(question8)

        question9 = Question(question_text="NLP'de köklemeye ne amaçla başvurulur?",
                             answer="Kelimeleri kök veya köken biçimine indirgeme",
                             choices="Kelimeleri tam biçimine genişletme|Doğru isimleri tanımlama|Kelimeleri kök veya köken biçimine indirgeme|Hece sayısını sayma",
                             exam_id=exam3.id)
        db.session.add(question9)

        db.session.commit()

    # Python uygulamalarında AI modelleri uygulama sınavı
    exam4 = Exam.query.filter_by(topic="Python uygulamalarında AI modelleri uygulama").first()
    if not exam4:
        exam4 = Exam(topic="Python uygulamalarında AI modelleri uygulama")
        db.session.add(exam4)
        db.session.commit()

        question10 = Question(question_text="AI uygulamalarında Flask'ın amacı nedir?",
                              answer="AI modellerini dağıtmak için web hizmetleri oluşturmak",
                              choices="Makine öğrenimi için veri ön işlemek|Veri görselleştirmek|AI modellerini dağıtmak için web hizmetleri oluşturmak|Sinir ağlarını uygulamak",
                              exam_id=exam4.id)
        db.session.add(question10)

        question11 = Question(question_text="Python'da doğal dil işleme (NLP) görevleri için genellikle hangi kütüphane kullanılır?",
                              answer="NLTK (Doğal Dil Kütüphanesi)",
                              choices="TensorFlow|NLTK (Doğal Dil Kütüphanesi)|OpenCV (Açık Bilgisayar Görüsü)|PyTorch",
                              exam_id=exam4.id)
        db.session.add(question11)

        question12 = Question(question_text="Makine öğreniminde aktarım öğrenmenin amacı nedir?",
                              answer="Bir görevden diğerine bilgi aktarımı yapmak",
                              choices="Bir görevden diğerine bilgi aktarımı yapmak|Öğrenme hızını optimize etmek|En iyi özellikleri seçmek|Model performansını iyileştirmek",
                              exam_id=exam4.id)
        db.session.add(question12)

        db.session.commit()

@app.route('/')
def home():
    global highest_score
    exams = Exam.query.all()
    return render_template('index.html', exams=exams, highest_score=highest_score)


@app.route('/exam/<int:exam_id>', methods=['GET', 'POST'])
def exam(exam_id):
    global highest_score
    exam = Exam.query.get_or_404(exam_id)
    questions = Question.query.filter_by(exam_id=exam_id).all()

    if request.method == 'POST':
        total_score = 0
        for question in questions:
            user_answer = request.form.get(str(question.id))
            if user_answer.lower() == question.answer.lower():  # Case insensitive comparison
                total_score += 1

        # Kullanıcının aldığı en yüksek puanı güncelle
        if total_score > highest_score:
            highest_score = total_score
        
        # Save the score to database (you can expand this part to save more details)
        return render_template('result.html', total_score=total_score, exam=exam, questions=questions, exams=Exam.query.all(), highest_score=highest_score)

    return render_template('exam.html', exam=exam, questions=questions, exams=Exam.query.all(), highest_score=highest_score)


if __name__ == '__main__':
    app.run(debug=True)