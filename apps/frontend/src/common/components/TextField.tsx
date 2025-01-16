/**
 * TextField モジュールコンポーネント
 */
import { JSX } from 'react';
import { Controller, Control, FieldValues, FieldPath, RegisterOptions } from 'react-hook-form';

import { TextField as MuiTextField, SxProps, Theme } from '@mui/material';

/**
 * React-Hook-Form に組み込んだ TextField モジュールコンポーネント用プロパティ
 */
type RHFProps<
  TFieldValues extends FieldValues = FieldValues,
  TName extends FieldPath<TFieldValues> = FieldPath<TFieldValues>,
> = {
  sx?: SxProps<Theme> | undefined;
  width?: number | undefined;
  label?: string | undefined;
  // maxLength?: number | undefined;
  controller: {
    control: Control<TFieldValues>;
    name: TName;
    rules?:
      | Omit<
          RegisterOptions<TFieldValues, TName>,
          'valueAsNumber' | 'valueAsDate' | 'setValueAs' | 'disabled'
        >
      | undefined;
  };
  disabled?: boolean;
  passwordType?: boolean;
  rows?: string | number | undefined;
  error?: boolean;
  onBlur?: React.FocusEventHandler<HTMLInputElement | HTMLTextAreaElement> | undefined;
};

/**
 * React-Hook-Form に組み込んだ TextField モジュールコンポーネント
 * @param sx sx
 * @param width コンポーネントの幅
 * @param label ラベル
 * @param maxLength 入力可能文字数
 * @param controller react-hook-formコントローラー情報
 * @param disabled 操作を無効とするかどうか
 * @param passwordType パスワードタイプとするかどうか
 * @param rows 行数
 * @param error エラーかどうか
 * @param onBlur 離脱イベントハンドラ
 * @returns {JSX.Element} JSX.Element
 */
export const RHFTextField = <
  TFieldValues extends FieldValues = FieldValues,
  TName extends FieldPath<TFieldValues> = FieldPath<TFieldValues>,
>({
  sx,
  width,
  label,
  // maxLength,
  controller,
  disabled = false,
  passwordType = false,
  rows,
  error,
  onBlur,
}: RHFProps<TFieldValues, TName>): JSX.Element => (
  <Controller
    name={controller.name}
    control={controller.control}
    rules={controller.rules}
    render={({ field, fieldState }) => (
      <MuiTextField
        sx={{ ...sx, width }}
        // slotProps={{ maxLength: { maxLength } }}
        label={label}
        variant="standard"
        inputRef={field.ref}
        {...field}
        disabled={disabled}
        type={passwordType ? 'password' : 'text'}
        rows={rows}
        multiline={!!rows}
        error={!!fieldState.error || error}
        helperText={fieldState.error?.message}
        onBlur={e => {
          field.onBlur();
          onBlur?.(e);
        }}
      />
    )}
  />
);
