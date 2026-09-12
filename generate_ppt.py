from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

def create_presentation():
    prs = Presentation()
    
    # Define slide layouts
    title_layout = prs.slide_layouts[0]
    bullet_layout = prs.slide_layouts[1]

    # Slide 1: Title
    slide1 = prs.slides.add_slide(title_layout)
    title = slide1.shapes.title
    subtitle = slide1.placeholders[1]
    title.text = "SmartQueue"
    subtitle.text = "The AI-Powered Virtual Queue & Triage Ecosystem\n\nScan. Track. Relax."

    # Slide 2: The Problem
    slide2 = prs.slides.add_slide(bullet_layout)
    title2 = slide2.shapes.title
    title2.text = "The Healthcare Waiting Crisis"
    body2 = slide2.placeholders[1]
    tf2 = body2.text_frame
    tf2.text = "Current waiting rooms are broken:"
    p = tf2.add_paragraph()
    p.text = "Cross-Infection: Crowded waiting rooms spread diseases."
    p.level = 1
    p = tf2.add_paragraph()
    p.text = "Anxiety & Uncertainty: Patients never know their true wait time."
    p.level = 1
    p = tf2.add_paragraph()
    p.text = "Staff Burnout: Front-desk staff are overwhelmed with manual entry."
    p.level = 1

    # Slide 3: The Solution
    slide3 = prs.slides.add_slide(bullet_layout)
    title3 = slide3.shapes.title
    title3.text = "The Solution: SmartQueue"
    body3 = slide3.placeholders[1]
    tf3 = body3.text_frame
    tf3.text = "A complete ecosystem for patients and doctors:"
    p = tf3.add_paragraph()
    p.text = "Frictionless Entry: Scan a QR code to join. No app download required."
    p.level = 1
    p = tf3.add_paragraph()
    p.text = "Freedom to wait anywhere: Track live position on your phone."
    p.level = 1
    p = tf3.add_paragraph()
    p.text = "Connects patient, doctor, and facility in real-time."
    p.level = 1

    # Slide 4: Key Features (The Wow Factor)
    slide4 = prs.slides.add_slide(bullet_layout)
    title4 = slide4.shapes.title
    title4.text = "Smarter Technology for Better Care"
    body4 = slide4.placeholders[1]
    tf4 = body4.text_frame
    tf4.text = "Key Innovations:"
    p = tf4.add_paragraph()
    p.text = "AI Symptom Triage: Google Gemini AI auto-routes patients to the correct department."
    p.level = 1
    p = tf4.add_paragraph()
    p.text = "Zero-Latency WebSockets: Phones and TV display boards update in exact real-time."
    p.level = 1
    p = tf4.add_paragraph()
    p.text = "Automated Voice Callouts: Smart TV board announces tokens automatically."
    p.level = 1

    # Slide 5: How It Works
    slide5 = prs.slides.add_slide(bullet_layout)
    title5 = slide5.shapes.title
    title5.text = "A Seamless Experience"
    body5 = slide5.placeholders[1]
    tf5 = body5.text_frame
    tf5.text = "The User Journey:"
    p = tf5.add_paragraph()
    p.text = "1. Patient scans QR code at the door."
    p.level = 1
    p = tf5.add_paragraph()
    p.text = "2. AI assigns Department & Estimated Wait Time."
    p.level = 1
    p = tf5.add_paragraph()
    p.text = "3. Doctor clicks 'Call Next' on dashboard."
    p.level = 1
    p = tf5.add_paragraph()
    p.text = "4. Patient's phone updates instantly & TV Board speaks."
    p.level = 1

    # Slide 6: Tech Stack
    slide6 = prs.slides.add_slide(bullet_layout)
    title6 = slide6.shapes.title
    title6.text = "Built for Scale & Speed (Tech Stack)"
    body6 = slide6.placeholders[1]
    tf6 = body6.text_frame
    tf6.text = "Modern infrastructure:"
    p = tf6.add_paragraph()
    p.text = "Frontend & Backend: Next.js 14, React, Tailwind CSS"
    p.level = 1
    p = tf6.add_paragraph()
    p.text = "Database: SQLite + Prisma ORM"
    p.level = 1
    p = tf6.add_paragraph()
    p.text = "Real-time Engine: Socket.io"
    p.level = 1
    p = tf6.add_paragraph()
    p.text = "Intelligence: Google Gemini AI API"
    p.level = 1
    
    # Slide 7: Future Scope & Demo
    slide7 = prs.slides.add_slide(title_layout)
    title7 = slide7.shapes.title
    subtitle7 = slide7.placeholders[1]
    title7.text = "Future Scope & Live Demo!"
    subtitle7.text = "Next steps: EHR Integration & Payments\n\nJUDGES: PLEASE SCAN THE QR CODE TO JOIN THE LIVE QUEUE NOW!"

    prs.save('SmartQueue_Pitch.pptx')
    print("PPT generated successfully!")

if __name__ == '__main__':
    create_presentation()
