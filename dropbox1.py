import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token= access_token
        
    def upload_file(self, file_from, file_to):
        dbx= dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
            
def main():
    access_token="sl.A1xHUqAYzW6L_ysReHSxQi5tgDq-4FA0A37nPkTuXiupVSFzkaVKWevd4SNb_KdpcDtPBBzDPETepQf1AwkVjZ7UPxs6MYpUfgzJqow2rUGpn1VzVcxx9MrlHN2XYpYs2HmtTpI"
    transferData = TransferData(access_token)
    file_from= "text.txt"
    file_to= '/test_dropbox/text.text'
    transferData.upload_file(file_from, file_to)
    print("file has been uploaded")

main()