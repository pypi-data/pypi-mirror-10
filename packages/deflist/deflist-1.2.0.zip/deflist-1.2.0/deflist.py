#��ԭ�й��ܻ����ϣ����Ӵ�ӡʱû����һ��Ƕ�׾�������ʾһ��TAB�Ʊ��(������һ���µĲ���level(0��1��2))
#Ϊ��ʹģ�鹦�ܱ�ĸ�Ϊ����ģ���бر������������е�һ����Ϊ��ѡ����Ϊ�����ȱʡֵ
def print_list(the_list,level=0):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_list(each_item,level+1) #ÿ��ӡһ�β���+1,��ʾ�´δ�ӡ�б�ʱ������һ��TAB�Ʊ��
        else:
            for tab_stop in range(level):
                  print("\t",end=" ")
            print(each_item)
