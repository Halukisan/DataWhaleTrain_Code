from langchain_community.document_loaders import UnstructuredMarkdownLoader

# 指定要读取的 Markdown 文件路径
markdown_file_path = "../data_base/knowledge_db/prompt_engineering/hello.md"
# 1. 简介 Introduction
# 创建 UnstructuredMarkdownLoader 实例
loader = UnstructuredMarkdownLoader(file_path=markdown_file_path)

# 使用 loader 加载 Markdown 文档
md_pages = loader.load()

# 打印加载的内容
for page in md_pages:
    print(page.page_content)
