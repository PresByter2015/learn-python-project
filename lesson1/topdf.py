import pdfkit

print('2222')

# pdfkit.from_url('http://google.com', 'out.pdf')
# pdfkit.from_file('test.html', 'out.pdf')
# pdfkit.from_string('Hello!', 'out.pdf')

body = """
    <html>
      <head>
        <meta name="pdfkit-page-size" content="Legal"/>
        <meta name="pdfkit-orientation" content="Landscape"/>
      </head>
      Hello World!
          <img src="http://lixing-develop.oss-cn-hangzhou.aliyuncs.com/large_file/1557201663002.jpg">

      </html>
    """
#       http://lixing-develop.oss-cn-hangzhou.aliyuncs.com/large_file/1557201663002.jpg
# with --page-size=Legal and --orientation=Landscape
config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
pdfkit.from_string(body, 'out.pdf', configuration=config)
