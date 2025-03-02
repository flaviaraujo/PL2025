import re

def markdown_to_html(md_text):
    # Cabeçalhos
    md_text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', md_text, flags=re.MULTILINE)
    
    # Bold
    md_text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', md_text)
    
    # Itálico
    md_text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', md_text)
    
    # Listas numeradas
    md_text = re.sub(r'^\d+\. (.+)$', r'<li>\1</li>', md_text, flags=re.MULTILINE)
    if '<li>' in md_text:
        md_text = '<ol>' + md_text + '</ol>'
    
    # Links
    md_text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', md_text)
    
    # Imagens
    md_text = re.sub(r'!\[(.+?)\]\((.+?)\)', r'<img src="\2" alt="\1"/>', md_text)
    
    return md_text

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    html_content = markdown_to_html(md_content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usagem: python tpc3.py input.md output.html")
    else:
        process_file(sys.argv[1], sys.argv[2])
