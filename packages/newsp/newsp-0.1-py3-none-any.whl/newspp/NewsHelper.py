from newspaper import Article
from newspp.ImageHelper import process_image
import tempfile,os,uuid,random
site_url = os.getenv('SITE_URL','https://hoablue.xyz')
class NewsHelper:
    def parse(self, url):
        article = Article(url)
        article.download()
        article.parse()
        new_top_image=""
        if article.top_image and len(article.top_image)>1 and "http" in article.top_image:
            new_top_image=process_image(article.top_image, article.title)
            if new_top_image:
                new_top_image = new_top_image.replace("\\","/")
                new_top_image = f"{site_url}/{new_top_image}"
        rs = {"title": article.title,
            "authors": article.authors,
            "text": article.text.split("\n"),
            "top_image": article.top_image, "new_top_image":new_top_image}
        return rs
    def make_body_html(self, arrtext):
        arr_html = []
        try:
            cut_begin=random.randint(0,3)
            cut_end=len(arrtext)-random.randint(0,3)
            arrtext=arrtext[cut_begin:cut_end]
            just_h2=False
            if len(arrtext)>3:
                for txt in arrtext:
                    if txt and len(txt)>1:
                        if len(txt) < 100 and not just_h2:
                            tmp_html = f"<h2>{txt}</h2>"
                            just_h2 = True
                        else:
                            tmp_html = f"<p>{txt}</p>"
                            just_h2 = False
                        arr_html.append(tmp_html)
        except:
            pass
        return arr_html

    def parse_auto(self,url):
        rs = None
        try:
            rs = self.parse(url)
            if rs and rs['title']:
                arr_html = self.make_body_html(rs['text'])
                if len(arr_html)>0:
                    if rs['new_top_image'] and len(rs['new_top_image'])>0:
                        tmp_img=f"<figure class=\"wp-block-image size-large\"><img src=\"{rs['new_top_image']}\" alt=\"{rs['title']}\"/></figure>"
                        arr_html = [tmp_img]+arr_html
                    tmp_folder = tempfile.gettempdir()
                    rs_file = os.path.join(tmp_folder, str(uuid.uuid4()) + ".txt")
                    with open(rs_file,"w",encoding="utf-8") as wf:
                        wf.writelines(arr_html)
                    cmd = f"wp --allow-root post create {rs_file} --post_title='{rs['title']}' --post_status='publish'"
                    cmd_meta = f" --meta_input='{{\"_knawatfibu_url\":\"{rs['new_top_image']}\",\"_knawatfibu_alt\":\"{rs['title']}\"}}'"
                    cmd += cmd_meta
                    print(cmd)
                    os.system(cmd)
                    os.remove(rs_file)
        except:
            pass
