from config import RunConfig


with open(RunConfig.base_path + '/tool/code_file/img_name.txt', 'r') as f:
    img_name = f.read()


class RunConfigPf:
    pf_url = "https://test.fontdo.com/platform/#/login"
    login_success_url = 'https://test.fontdo.com/platform/#/main/home'
    img_name = img_name
    img_path = RunConfig.base_path+'/tool/code_file/'+img_name


if __name__ == '__main__':
    print("")