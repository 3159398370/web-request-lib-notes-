### ⚙️ 一、配置与初始化
| 命令                                    | 说明           | 示例                                                 |
| --------------------------------------- | -------------- | ---------------------------------------------------- |
| `git config --global user.name "姓名"`  | 全局用户名     | `git config --global user.name "张三"`               |
| `git config --global user.email "邮箱"` | 全局邮箱       | `git config --global user.email "zhang@example.com"` |
| `git init`                              | 初始化本地仓库 | `git init my-project`                                |
| `git clone <url>`                       | 克隆远程仓库   | `git clone https://github.com/user/repo.git`         |
| `git config --global alias.st status`   | 设置命令别名   | `git st` 代替 `git status` [1,4](@ref)               |

---

### 📂 二、文件状态管理
| 命令                 | 作用             | 常用参数                              |
| -------------------- | ---------------- | ------------------------------------- |
| `git status`         | 查看工作区状态   | `-s`（简洁模式）                      |
| `git add <file>`     | 添加文件到暂存区 | `.`（所有文件）、`*.txt`（通配符）    |
| `git restore <file>` | 撤销工作区修改   | `--staged`（取消暂存）                |
| `git rm <file>`      | 删除文件并暂存   | `--cached`（保留本地文件）[1,2](@ref) |

---

### 💾 三、提交操作
```bash
# 基础提交
git commit -m "描述信息"          # 提交暂存区
git commit -am "描述信息"         # 跳过add直接提交修改[4](@ref)

# 修正提交
git commit --amend               # 修改上次提交（信息/文件）
git commit --amend --no-edit     # 追加文件到上次提交[3,4](@ref)
```

### 🌿 四、分支管理

|           命令           |      功能      |              替代方案              |
| :----------------------: | :------------: | :--------------------------------: |
|       `git branch`       |    查看分支    |    `-v`（详情）、`-a`（含远程）    |
| `git switch -c <branch>` | 创建并切换分支 | `git checkout -b <branch>`（旧版） |
|   `git merge <branch>`   |    合并分支    |     `--no-ff`（保留分支历史）      |
| `git branch -d <branch>` |    删除分支    |     `-D`（强制删除未合并分支）     |

------

### 🌐 五、远程协作

```
git push origin main             # 推送到远程main分支
git push -u origin main          # 首次推送并设置跟踪
git pull origin main             # 拉取远程变更（= fetch + merge）
git fetch --all                  # 获取远程更新但不合并[1,8](@ref)

# 远程分支操作
git push --delete origin dev     # 删除远程分支
git remote set-url origin <url>  # 修改远程仓库地址[4,5](@ref)
```

------

### ⏪ 六、撤销与重置

|      场景      |             命令              |        警告        |
| :------------: | :---------------------------: | :----------------: |
| 丢弃工作区修改 |     `git restore <file>`      |     不可恢复！     |
|  取消暂存文件  | `git restore --staged <file>` |   保留工作区修改   |
|   软回退提交   |   `git reset --soft HEAD~1`   |  保留修改到暂存区  |
|  **强制回退**  |   `git reset --hard HEAD~1`   | **永久丢失修改！** |

------

### 📦 七、储藏（Stash）

```
git stash push -m "描述"        # 暂存当前修改
git stash list                  # 查看暂存列表
git stash pop                   # 恢复并删除最新暂存
git stash apply stash@{0}       # 恢复指定暂存不删除[3,4](@ref)
```

------

### 🔍 八、查看历史

```
git log                         # 完整提交历史
git log --oneline --graph       # 图形化简洁历史
git blame <file>                # 查看文件逐行修改者
git diff HEAD~3..HEAD           # 比较最近3次提交差异[1,8](@ref)
```

------

### 🏷️ 九、标签管理

```
git tag v1.0.0                  # 创建轻量标签
git tag -a v1.0.0 -m "发布说明" # 含注释的标签
git push origin v1.0.0          # 推送标签到远程[3,4](@ref)
```

------

### 🔄 工作流策略建议

1. **分支策略**

   - `main`：稳定版本，仅用于发布

   - `dev`：集成测试分支

   - ```
     feature/xxx
     ```

     ：功能开发分支

     

2. **合并策略**

   - **`merge`**：保留分支历史（团队协作首选）

   - **`rebase`**：线性历史（本地整理提交）

   - ⚠️ 禁止对

     公共分支

     执行rebase！

     

3. **提交规范**

   ```
   git commit -m "feat: 新增登录功能"   # 功能
   git commit -m "fix: 修复支付bug"     # 修复
   git commit -m "docs: 更新API文档"    # 文档[4](@ref)
   ```

------

### 📌 终极速查表

|     场景     |              命令              |
| :----------: | :----------------------------: |
|  **初始化**  |         `init` `clone`         |
| **日常操作** | `add` `commit` `status` `diff` |
| **分支操作** |   `branch` `switch` `merge`    |
| **远程协作** |     `push` `pull` `fetch`      |
| **紧急撤销** |   `restore` `reset` `revert`   |
| **临时保存** |            `stash`             |
| **历史追溯** |         `log` `blame`          |