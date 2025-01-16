import { FieldValues, FieldPath } from 'react-hook-form';

/**
 * HTTPレスポンス情報
 * @param TFieldValues フィールド値の型
 * @param status ステータス
 * @param error エラー情報
 */
class HttpResponse<TFieldValues extends FieldValues = FieldValues> {
  status: 'SUCCESS' | 'FAIRLURE';
  error: {
    message: string;
    fieldname: FieldPath<TFieldValues>;
  } | null;

  /**
   * コンストラクタ
   * @param param HTTPレスポンス情報
   * @param param.status ステータス
   * @param param.error エラー情報
   * @throws 失敗の際にHTTPレスポンス情報にエラー情報が設定されていない場合
   */
  constructor(param: {
    status: 'SUCCESS' | 'FAIRLURE';
    error: {
      message: string;
      fieldname: string;
    } | null;
  }) {
    if (param.status === 'SUCCESS') {
      this.status = 'SUCCESS';
      this.error = null;
      return;
    }

    if (param.status === 'FAIRLURE' && param.error) {
      this.status = 'FAIRLURE';
      this.error = {
        message: param.error.message,
        fieldname: param.error.fieldname as FieldPath<TFieldValues>,
      };
      return;
    }

    throw new Error('HTTPレスポンス情報にエラー情報が設定されていません');
  }
}
export default HttpResponse;
