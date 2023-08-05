# state-machine-py

状態遷移マシン

## Install

```shell
# Windows
python.exe -m pip install state_machine_py
```

## Example

* Homepage
  * 📂tests
    * 📂[rock_paper_scissors](https://github.com/muzudho/state-machine-py/tree/main/tests/rock_paper_scissors) - じゃんけん
    * 📂[edge_walk](https://github.com/muzudho/state-machine-py/tree/main/tests/edge_walk) - ツリー構造のエッジ
    * 📂[two_machines_catchball](https://github.com/muzudho/state-machine-py/tree/main/tests/two_machines_catchball) - 複数のステートマシンの実行

```shell
python.exe -m tests.rock_paper_scissors.main
python.exe -m tests.edge_walk.main
python.exe -m tests.two_machines_catchball.main
```

## Auto generation

定義ファイルの自動生成

```shell
# Windows
python.exe -m state_machine_py.const_py_maker "tests/rock_paper_scissors/data/const.json" "tests/rock_paper_scissors/data/auto_gen/const.json"
#                                             ------------------------------------------- ----------------------------------------------------
#                                             Input                                        Output
```

## Skill up

* 📖 [State machine Practice](https://github.com/muzudho/py-state-machine-practice)
