import axios from '@/config/axios';

interface LoginResponse {
  accessToken: string;
  tokenType: string;
}

interface LoginRequest {
  username: string;
  password: string;
}

export const login = async (request: LoginRequest): Promise<LoginResponse> => {
  try {
    console.log('リクエスト：', request);
    const response = await axios.post<LoginResponse>('/auth/token', request);
    console.log('レスポンス：', response);
    return response.data;
  } catch {
    throw new Error('ログインに失敗しました');
  }
};
