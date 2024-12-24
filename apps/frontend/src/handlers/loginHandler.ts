import axios from '@/config/axios';

interface LoginResponse {
  accessToken: string;
  tokenType: string;
}

interface LoginRequest {
  username: string;
  password: string;
}

export const login = async (request: LoginRequest): Promise<void> => {
  try {
    console.log('リクエスト：', request);
    const formData = new URLSearchParams();
    formData.append('username', request.username);
    formData.append('password', request.password);

    const response = await axios.post<LoginResponse>('/auth/token', formData, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      withCredentials: true,
    });
    console.log('レスポンス：', response);
  } catch (error) {
    console.error('ログインに失敗しました', error);
    throw new Error('ログインに失敗しました');
  }
};

export const removeToken = (): void => {
  document.cookie = 'accesss_token=; max-age=0';
};
