import axios, { isAxiosError } from '@/config/axios';
import HttpResponse from '@/models/httpResponse';

interface LoginResponse {
  accessToken: string;
  tokenType: string;
}

interface LoginRequest {
  username: string;
  password: string;
}

/**
 * ログイン処理
 * @param request ログインリクエスト情報
 * @throws HttpResponse HTTPレスポンス情報
 */
export const login = async (request: LoginRequest): Promise<HttpResponse> => {
  try {
    const response = await axios.post<LoginResponse>(
      '/auth/login',
      {
        username: request.username,
        password: request.password,
      },
      {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        withCredentials: true,
      }
    );

    console.log('ログインに成功しました:', response);
    // アクセストークンをセッションストレージに保存
    sessionStorage.setItem('accessToken', response.data.accessToken);

    return new HttpResponse({ status: 'SUCCESS', error: null });
  } catch (error) {
    if (isAxiosError(error)) {
      const { response } = error;
      console.error('ログインに失敗しました', response);
      return new HttpResponse({
        status: 'FAIRLURE',
        error: {
          message: response?.data.detail.message,
          fieldname: response?.data.detail.fieldname,
        },
      });
    }
    throw Error('AxiosErrorではありません');
  }
};

/**
 * ログアウト処理
 */
export const logout = async (): Promise<void> => {
  const token = sessionStorage.getItem('access_token');
  if (!token) {
    console.error('トークンが見つかりません');
    return;
  }

  try {
    await axios.post('/auth/logout', null, {
      headers: { Authorization: `Bearer ${token}` },
      withCredentials: true,
    });
    sessionStorage.removeItem('accessToken');
  } catch (error) {
    console.error('ログアウトに失敗しました', error);
  }
};

// export const removeToken = (): void => {
//   document.cookie = 'accesss_token=; max-age=0';
// };
