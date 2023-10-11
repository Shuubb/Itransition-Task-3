import secrets
import hmac

class HMACGenerator:
    def __init__(self):
        self.key = self.generate_key()

    def generate_key(self):
        return secrets.token_hex(256 // 8)

    def compute_hmac(self, user_input):
        hmac_obj = hmac.new(self.key.encode('utf-8'), user_input.encode('utf-8'), 'sha256')
        return hmac_obj.hexdigest()
