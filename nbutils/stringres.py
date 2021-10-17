from pydantic import BaseSettings

FULL_SPACE = '　'  # \u3000，全角空格

EMOJI_WARNING = '⚠'
EMOJI_FAILED = '✘'
EMOJI_SUCCEED = '✔'
EMOJI_QUESTION = '�'


class StringRes(BaseSettings):
    MSG_UNKNOWN_CMD = "未知命令 '{cmd}'。\n" \
                      "请使用 '/help {sv_name}' 获取可用命令列表。"

    MSG_NO_CMD_INPUT = "未选择命令。\n" \
                       "请使用 '/{sv_name} [命令]' 调用命令，\n" \
                       "或使用 '/help {sv_name}' 获取可用命令列表。"

    MSG_SERVICE_USAGE = "==== <{sv_name}> 服务帮助 ====\n\n" \
                        "➢ 说明文档\n{doc}\n\n" \
                        "➢ 命令列表\n{cmds_list}\n\n" \
                        "使用 '/help {sv_name} [命令]' 查看命令帮助。\n" \
                        "使用 '/{sv_name} [命令] [参数]' 调用此命令。' "

    EXPR_CALL_SV_DIRECTLY = "<直接调用>"
    EXPR_NOT_AVAILABLE = "（无可用信息）"
    EXPR_NO_CMDS_IN_SV = "（无可用命令）"

    FORMAT_CMDS_LIST = " » {cmd}\n" \
                       + FULL_SPACE + "{desc}"

    FORMAT_BASIC_MSG = " <{name}>: {msg}" # {time} -> %H:%M
    FORMAT_SUCC_MSG = EMOJI_SUCCEED + FORMAT_BASIC_MSG
    FORMAT_FAILED_MSG = EMOJI_FAILED + FORMAT_BASIC_MSG
    FORMAT_WARNING_MSG = EMOJI_WARNING + FORMAT_BASIC_MSG
    FORMAT_QUESTION_MSG = EMOJI_QUESTION + FORMAT_BASIC_MSG


Rstr = StringRes()
