import { FieldValues, FieldPath } from 'react-hook-form';

/**
 * バリデーションエラー情報
 * @param message エラーメッセージ
 * @param fieldname エラーが発生したフィールド名
 */
class ValidationError<TFieldValues extends FieldValues = FieldValues> extends Error {
  message: string;
  fieldname: FieldPath<TFieldValues>;

  constructor(message: string, fieldname: string) {
    super(message);
    this.message = message;
    this.fieldname = fieldname as FieldPath<TFieldValues>;
  }
}
export default ValidationError;
