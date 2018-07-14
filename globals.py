#coding=utf-8

# superusers: ��Ȩ��ִ����������� QQ ��
# whitelist: �����б��е��˽��йؼ��ʽ��ԡ��ؼ��ʻظ����Լ�Ⱥ��Ƭ���

host = '0.0.0.0'
port = 8080
connect_to = 'http://127.0.0.1:5700/'
access_token = ''
secret = ''

me = 10000
# ��¼�ţ������˺ţ�
bugs_fixer = 10000
# ��� traceback ˽�ĸ���� QQ ��
active_groups = []
# ���õ�Ⱥ���б�

enable_group_in_auto_check = True
# ���Ϊ�棬���Զ���ѧ��������ȷ����׼��Ⱥ
card_pattern = R"\d{2}[\- ]+\w+[\- ]+\w+"
# Ⱥ��Ƭ pattern

auto_reply = [
    [
        ["key1", "key2"],
        ["key3", "key4", "key5"],
        "�ظ�����"
    ],
    # ...
]
# �Զ��ظ��ļ���Ϊ����ؼ��ʣ��������ؼ��ʾ����ٳ���һ������ظ�֮

prohibited_words = ["Ůװ", "Ĥ"]
prohibited_duration = 2

prompts = dict(
    ping = 'pong!',
    why_at_me = '@�Ҹ��',
    prohibited_occurred = '��Ⱥ��Ĥ��Ůװ�������������侲�侲~',
    unknown_command = 'δ֪���������%help��%menu�鿴����',
    need_more_arguments = 'ȱ�ٱ�Ҫ����',
    must_digits_or_CQat = '���������� QQ �Ż���һ�γɹ��� @��',
    must_digits = '����������������',
    wrong_argument = '��������',
    permission_needed = '��û��ִ�д������Ȩ��',
    group_request_plz_fill = '����������д���ѧ������',
    group_request_plz_correct = '����ȷ��д���ѧ������',
    request_change_card = '���Ⱥ��Ƭ�����Ϲ淶�����޸�',
    kick_for_card_incorrect = '�������Ⱥ��Ƭ�����Ϲ淶�����ѱ��Ƴ�Ⱥ\n'
                              '��ΪȺ�ǳƸ��µ�Ƶ�ʺܵͣ�����Ҳ���ǲ�����\n'
                              '�����˶���������������ʮ�ֱ�Ǹ�����¼�Ⱥ����~',
    success_ban = '���Գɹ���[CQ:at,qq={to}] �������� {duration} ����',
    success_whole_ban = '�ѿ���ȫԱ���ԣ���Ȩ�޵��˿�˽�Ļظ� /unban Ⱥ�� ���ȫԱ����',
    success_unban = '����ɹ����� [CQ:at,qq={to}] �Ľ����ѱ�����',
    success_whole_unban = 'ȫԱ�����ѹر�',
    success_auto_check_card = 'Ⱥ��Ƭ������',
    private_preparing = '˽��ģ�黹û���дʲô����',
    menu = '\n'.join(['֧����������',
                      '/ban* [QQ/@] [����]',
                      '���ԣ�Ĭ��2min��ʡ��QQ��ȫԱ����',
                      '/unban* [QQ/@]',
                      '������ԣ�ʡ��QQ��ر�ȫԱ����',
                      '/autocheck* [to] �� /autokick*',
                      '���Ⱥ��Ƭ�淶���ǰ��@�����ѣ�����ֱ������',
                      '���ã���ΪȺ��Ƭ�ܾòŻ����һ��',
                      'to��������public��private����Ⱥ���˽�����ѣ�Ĭ��Ⱥ��',
                      '/menu /ping',
                      '���ý���\n',
                      '��*������ҪȨ��']),
    welcome_newbie = "Hi����ӭ���뱾Ⱥ~",
    black_house = "���ѱ����ý��ԣ��鷳˽�Ĺ���Աѯ�ʾ�������",
    fmtstr_s = "flag{welcome_to_vidar}����������",
    fmtstr_x = "66",#���Ķ�Ӧ666C61677B77656C636F6D655F746F5F76696461727DCCCCCCCCCCCCCCCCCCCC
    fmtstr_n = "����������Ҿ�������"
)

permission_commands = ["ban", "unban", "autocheck", "autokick"]

info_check_url = 'http://example.com/api/student/info/{}'
