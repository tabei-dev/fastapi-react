/**
 * axios拡張モジュール
 */
import axios, { AxiosInstance, isAxiosError } from 'axios';
import { camelCase } from 'change-case';

export const ACCESS_TOKEN = 'accesss_token' as const;

/**
 * axiosインスタンスを生成します。
 */
const Axios: AxiosInstance = axios.create({
  baseURL: import.meta.env.VITE_URL,
  // headers: { 'X-Requested-With': 'XMLHttpRequest' },
  withCredentials: true,
});

/**
 * レスポンスデータがオブジェクトかどうかを判定します。
 * @param responseData レスポンスデータ
 * @returns レスポンスデータがオブジェクトの場合はtrue、それ以外の場合はfalse
 */
const isObject = (responseData: unknown) =>
  Object.prototype.toString.call(responseData).slice(8, -1).toLowerCase() === 'object';

/**
 * レスポンスデータのキーをスネークケースからキャメルケースに変換します。
 * @param responseData レスポンスデータ
 */
// eslint-disable-next-line @typescript-eslint/no-explicit-any
const convertSnakeToCamel = (responseData: any) => {
  if (Array.isArray(responseData)) {
    responseData.forEach(t => convertSnakeToCamel(t));
  }
  if (isObject(responseData)) {
    Object.keys(responseData).forEach(key => {
      if (isObject(responseData[key]) || Array.isArray(responseData[key])) {
        convertSnakeToCamel(responseData[key]);
      }

      // キーをキャメルケースに変換（変換後もアンダースコアが付与されている場合があるのでこれを除去）
      const camelCaseKey = camelCase(key).replace('_', '');
      // 変換前と変換後のキーがまったく同じときにキーのオブジェクトを削除すると
      // 両方のキーのオブジェクトが削除されてしまうので変換前と変換後のキーが同じ場合は何もしない
      if (key === camelCaseKey) return;

      // 値をスネークケースのキーのオブジェクトからキャメルケースのキーのオブジェクトに設定しなおす
      responseData[camelCaseKey] = responseData[key];
      // スネークケースのキーのオブジェクトを削除
      delete responseData[key];
    });
  }
};

/**
 * リクエストインターセプター
 * すべてのリクエストでトークンが付与されるようにします。
 */
Axios.interceptors.request.use(
  request => {
    const token = sessionStorage.getItem(ACCESS_TOKEN);
    request.headers.Authorization = token ? `Bearer ${token}` : '';
    return request;
  },
  error => Promise.reject(error)
);

/**
 * レスポンスインターセプター
 * レスポンス時にスネークケースをキャメルケースに変換します。
 */
Axios.interceptors.response.use(response => {
  if (response.data) {
    convertSnakeToCamel(response.data);
  }
  return response;
});

export default Axios;

export { isAxiosError };
