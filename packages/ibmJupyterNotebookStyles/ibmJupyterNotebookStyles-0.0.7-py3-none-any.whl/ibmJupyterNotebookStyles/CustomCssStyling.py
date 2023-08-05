
from ibmJupyterNotebookStyles.StylingBase import StyleComponent
import IPython.core.display


class CustomCssStyling(StyleComponent):
    def __init__(self):
        self.html: IPython.core.display.HTML = None

    def apply(self) -> None:
        self.html = IPython.core.display.HTML("""
<style type="text/css">
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&family=IBM+Plex+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap');

div.jp-RenderedHTMLCommon, div.text_cell_render {
font-family: 'IBM Plex Sans', sans-serif;
width: inherit; 
}

/* Set the size of the headers */
div.jp-RenderedHTMLCommon h1,
div.text_cell_render h1 {
    font-size: 42px;
    font-weight: 300;
    line-height: 1.199;
    letter-spacing: 0px;
}

div.jp-RenderedHTMLCommon h2,
div.text_cell_render h2 {
    font-size: 32px;
    font-weight: 400;
    line-height: 1.25;
    letter-spacing: 0px;
}

div.jp-RenderedHTMLCommon h3,
div.text_cell_render h3 {
    font-size: 28px;
    font-weight: 400;
    line-height: 1.29;
    letter-spacing: 0px;
}

div.jp-RenderedHTMLCommon h4,
div.text_cell_render h4 {
    font-size: 20px;
    font-weight: 400;
    line-height: 1.4;
    letter-spacing: 0px;
}

div.jp-RenderedHTMLCommon h5,
div.text_cell_render h5 {
    font-size: 16px;
    font-weight: 600;
    line-height: 1.375;
    letter-spacing: 0px;
}

div.jp-RenderedHTMLCommon h6,
div.text_cell_render h6 {
    font-size: .14px;
    font-weight: 600;
    line-height: 1.29;
    letter-spacing: .16px;
}

div.jp-RenderedHTMLCommon p,
div.text_cell_render p {
    font-size: 16px;
    font-weight: 400;
    line-height: 1.5;
    letter-spacing: 0px;
}

div.jp-RenderedHTMLCommon a,
div.jp-RenderedHTMLCommon a:link ,
div.text_cell_render a {
    color: #0062fe!important;
}

div.jp-RenderedHTMLCommon em,
div.text_cell_render em {
    font-style: italic;
}

div.jp-RenderedHTMLCommon strong,
div.text_cell_render strong {
    font-weight: 600;
}

.CodeMirror-code,
.CodeMirror {
     font-family: 'IBM Plex Mono', Consolas, monospace;
}

.rendered_html ol {list-style:decimal; margin: 1em 2em;}

/* Table of contents */
div#toc {
    font-family: 'IBM Plex Sans', sans-serif;
}

/* Code */
code {
    font-family: 'IBM Plex Mono, Consolas, monospace;
}

bdi {
    font-family: 'IBM Plex Mono', Consolas, monospace;
}

div.cell.selected:before, div.cell.selected.jupyter-soft-selected:before {
    position: absolute;
    display: block;
    top: -1px;
    left: -1px;
    width: 5px;
    height: calc(100% + 2px);
    content: '';
    background: #0f62fe;
}

.edit_mode div.cell.selected:before{
    background: #42be65!important;
}

.edit_mode div.cell.selected{
    border-color: #42be65!important;
}


</style>
""")
