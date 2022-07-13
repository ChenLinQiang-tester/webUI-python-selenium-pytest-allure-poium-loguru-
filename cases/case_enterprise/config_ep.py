from config import RunConfig


with open(RunConfig.base_path + '/tool/code_file/img_name.txt', 'r') as f:
    img_name = f.read()


class RunConfigEp:
    ep_url = "https://5g.fontdo.com/test/enterprise//#/login"
    login_success_url = 'https://5g.fontdo.com/enterprise//#/'
    img_name = img_name
    img_path = RunConfig.base_path+'/tool/code_file/'+img_name


if __name__ == '__main__':
    print("")