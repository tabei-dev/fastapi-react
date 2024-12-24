/**
 * スネークケースで定義されているDBのカラムを
 * フロントエンド側のキャメルケースに変換するためのaxios拡張
 */
import axios, { AxiosInstance } from 'axios';
import { camelCase } from 'change-case';

const Axios: AxiosInstance = axios.create({
  baseURL: import.meta.env.VITE_URL,
  // headers: { 'X-Requested-With': 'XMLHttpRequest' },
  withCredentials: true,
});

const isObject = (target: unknown) =>
  Object.prototype.toString.call(target).slice(8, -1).toLowerCase() === 'object';

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const convertSnakeToCamel = (target: any) => {
  if (Array.isArray(target)) {
    target.forEach(t => convertSnakeToCamel(t));
  }
  if (isObject(target)) {
    Object.keys(target).forEach(key => {
      if (isObject(target[key]) || Array.isArray(target[key])) {
        convertSnakeToCamel(target[key]);
      }

      // キーをキャメルケースに変換（変換後もアンダースコアが付与されている場合があるのでこれを除去）
      const camelCaseKey = camelCase(key).replace('_', '');
      // 変換前と変換後のキーがまったく同じときにキーのオブジェクトを削除すると
      // 両方のキーのオブジェクトが削除されてしまうので変換前と変換後のキーが同じ場合は何もしない
      if (key === camelCaseKey) return;

      // 値をスネークケースのキーのオブジェクトからキャメルケースのキーのオブジェクトに設定しなおす
      target[camelCaseKey] = target[key];
      // スネークケースのキーのオブジェクトを削除
      delete target[key];
    });
  }
};

Axios.interceptors.request.use(request => {
  const token = localStorage.getItem('auth_token');
  request.headers.Authorization = token ? `Bearer ${token}` : '';
  return request;
});

Axios.interceptors.response.use(response => {
  if (response.data) {
    convertSnakeToCamel(response.data);
  }
  return response;
});

export default Axios;
