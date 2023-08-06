"""ibm-delete: 删除 IBM COS 中的文件
dependencies = ["arrow", "ibm-cos-sdk"] (另外还依赖 recipes/common_ibm.py)

本插件用于删除原本由 ibm-upload 上传到 IBM COS 中的文件。

https://github.com/ahui2016/ffe/raw/main/recipes/common_ibm.py
https://github.com/ahui2016/ffe/raw/main/recipes/ibm-delete.py
"""

# 每个插件都应如上所示在文件开头写简单介绍，以便 "ffe install --peek" 功能窥视插件概要。

import arrow
from ffe.model import (
    Recipe,
    ErrMsg,
    names_limit,
)
from ffe.util import get_proxies
from common_ibm import (
    FilesSummary,
    files_summary_name,
    get_config,
    get_files_summary,
    get_ibm_resource,
)

# 每个插件都必须继承 model.py 里的 Recipe
class IBMDelete(Recipe):
    @property  # 必须设为 @property
    def name(self) -> str:
        return "ibm-delete"

    @property  # 必须设为 @property
    def help(self) -> str:
        return """
[[tasks]]
recipe = "ibm-delete"  # 删除 IBM COS 中的文件
names = [              # 文件的前缀，每次最多只可填写 1 个前缀
    '20220115'         # 使用 ibm-upload 上传文件时会自动添加日期前缀
]                      # 如果 names 为空，则打印文件数量统计结果

[tasks.options]
names = []             # 只有当多个任务组合时才使用此项代替命令行输入

# 本插件与 ibm-upload 搭配使用，用于删除由 ibm-upload 上传的文件。
"""

    @property  # 必须设为 @property
    def default_options(self) -> dict:
        return dict(
            names=[],
        )

    def validate(self, names: list[str], options: dict) -> ErrMsg:
        """初步检查参数（比如文件数量与是否存在），并初始化以下项目：

        - self.prefix
        """
        # 要在 dry_run, exec 中确认 is_validated
        self.is_validated = True

        # 优先采用 options 里的 names, 方便多个任务组合。
        options_names = options.get("names", [])
        if options_names:
            names = options_names

        # set self.prefix
        names, err = names_limit(names, 0, 1)
        if err:
            return err
        if names:
            self.prefix = names[0]
        else:
            self.prefix = ""

        return ""

    def dry_run(self) -> ErrMsg:
        assert self.is_validated, "在执行 dry_run 之前必须先执行 validate"

        cfg_ibm = get_config()
        cos = get_ibm_resource(cfg_ibm, get_proxies())
        bucket_name = cfg_ibm["bucket_name"]

        # 如未指定前缀，则打印 files-summary
        if not self.prefix:
            print("Retrieving files summary...")
            summary: FilesSummary = get_files_summary(
                cos, bucket_name, files_summary_name
            )
            total = 0
            for date, n in summary["date_count"].items():
                print(f"{arrow.get(date).format('YYYY-MM-DD')}  {n}")
                total += n
            print(f"\nTotal: {total} files")
            return ""
        return ""

    def exec(self) -> ErrMsg:
        assert self.is_validated, "在执行 exec 之前必须先执行 validate"
        return ""


__recipe__ = IBMDelete
