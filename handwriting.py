import pywhatkit as pyw # installed

txt='''In 34 Seconds WhatsApp will open and after 15 Seconds Message will be Delivered!
In 34 Seconds WhatsApp will open and after 15 Seconds Message will be Delivered!'''

# pyw.text_to_handwriting(txt)                             # black
pyw.text_to_handwriting(txt,'converted.png',[0,0,138])     # blue
# pyw.text_to_handwriting(txt,'converted1.png',[255,0,0,]) # red

print('done')