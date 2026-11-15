from google import genai

client = genai.Client()  # يقرأ GEMINI_API_KEY تلقائياً

def build_prompt(product, description, audience, platform, tone):
    return f"""أنت خبير تسويق رقمي محترف.
اكتب إعلاناً للمنتج التالي:

- اسم المنتج: {product}
- الوصف: {description}
- الجمهور المستهدف: {audience}
- المنصة: {platform}
- نبرة الإعلان: {tone}

المطلوب:
1. عنوان جذاب (سطر واحد)
2. نص الإعلان (3-4 أسطر)
3. Call to Action واضح
4. 5 هاشتاغات مناسبة

اكتب بالعربية، وراعِ أسلوب المنصة المذكورة."""

def generate_ad(product, description, audience, platform, tone):
    prompt = build_prompt(product, description, audience, platform, tone)
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
    )
    return response.text

if __name__ == "__main__":
    try:
        result = generate_ad(
            product="عطر ليالي بغداد",
            description="عطر شرقي فاخر برائحة العود والورد، يدوم 12 ساعة",
            audience="نساء ورجال من 25 إلى 45 سنة",
            platform="انستغرام",
            tone="فخم وأنيق",
        )
        print(result) 
    except Exception as e:
        print("الخطأ:", type(e).__name__)
        print(e)