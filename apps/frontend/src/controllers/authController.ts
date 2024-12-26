import axios from '@/config/axios';

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
 */
export const login = async (request: LoginRequest): Promise<void> => {
  try {
    // console.log('リクエスト：', request);
    const response = await axios.post<LoginResponse>(
      '/auth/token',
      {
        username: request.username,
        password: request.password,
      },
      {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        withCredentials: true,
      }
    );

    sessionStorage.setItem('accessToken', response.data.accessToken);

    // console.log('レスポンス：', response);
  } catch (error) {
    console.error('ログインに失敗しました', error);
    // throw new Error('ログインに失敗しました');
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
    // throw new Error('ログアウトに失敗しました');
  }
};

// export const removeToken = (): void => {
//   document.cookie = 'accesss_token=; max-age=0';
// };
