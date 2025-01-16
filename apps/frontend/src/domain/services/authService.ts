// import { useSetRecoilState } from 'recoil';

import axios, { isAxiosError, ACCESS_TOKEN } from '@/common/config/axios';
// import HttpResponse from '@/common/models/httpResponse';
import { EMPTY, Empty } from '@/common/config/consts';
import ValidationError from '@/common/models/validationError';
import Auth from '@/domain/models/auth';
// import { authState } from '@/domain/recoil/recoil';

interface LoginResponse {
  accessToken: string;
  tokenType: string;
  username: string;
  email: string;
  roleCls: string;
}

interface LoginRequest {
  username: string;
  password: string;
}

class AuthService {
  private static instance: AuthService;
  private auth: Auth | Empty = EMPTY;

  private constructor() {}

  public static getInstance(): AuthService {
    if (!AuthService.instance) {
      AuthService.instance = new AuthService();
    }
    return AuthService.instance;
  }

  /**
   * ログイン処理
   * @param request ログインリクエスト情報
   * @throws ValidationError バリデーションエラー情報
   */
  public async login(request: LoginRequest): Promise<void> {
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
      sessionStorage.setItem(ACCESS_TOKEN, response.data.accessToken);
      // 認証情報を生成して内部に保持
      this.setAuth({
        username: response.data.username,
        email: response.data.email,
        roleCls: response.data.roleCls,
      });
    } catch (error) {
      if (isAxiosError(error)) {
        const { response } = error;
        console.error('ログインに失敗しました', response);
        throw new ValidationError(response?.data.detail.message, response?.data.detail.fieldname);
      }
      throw Error('ログインに失敗しました');
    }
  }

  /**
   * ログアウト処理
   */
  public async logout(): Promise<void> {
    this.removeAuth();

    const token = sessionStorage.getItem(ACCESS_TOKEN);
    if (!token) {
      console.error('トークンが見つかりません');
      return;
    }

    try {
      await axios.post('/auth/logout', null, {
        headers: { Authorization: `Bearer ${token}` },
        withCredentials: true,
      });
      sessionStorage.removeItem(ACCESS_TOKEN);
    } catch (error) {
      console.error('ログアウトに失敗しました', error);
    }
  }

  /**
   * 認証情報を取得します。
   * @returns 認証情報
   */
  public getAuth(): Auth {
    if (!this.auth) {
      throw Error('認証情報が保持されていません');
    }
    return this.auth;
  }

  /**
   * 認証情報を設定します。
   * @param auth 認証情報
   */
  private setAuth(auth: Auth): void {
    this.auth = auth;
  }

  /**
   * 認証情報を削除します。
   */
  private removeAuth(): void {
    this.auth = EMPTY;
  }
}
export default AuthService.getInstance();

// export const removeToken = (): void => {
//   document.cookie = 'accesss_token=; max-age=0';
// };
