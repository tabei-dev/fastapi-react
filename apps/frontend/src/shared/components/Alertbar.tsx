/**
 * アラートバー モジュールコンポーネント
 */
import { JSX } from 'react';

import { Snackbar, Alert, AlertColor } from '@mui/material';

/**
 * アラート情報
 */
export type AlertInfo = {
  open: boolean;
  message: string;
  severity?: AlertColor | undefined;
  afterType?: 'none' | 'pageInit' | 'fetchData' | 'pageClose';
};

type Props = {
  open: boolean;
  message: string;
  severity: AlertColor;
  autoHideDuration?: number | null;
  onClose: () => void;
};

/**
 * アラートバー
 * @param open オープンフラグ
 * @param message メッセージ
 * @param severity 警告レベル
 * @param autoHideDuration 自動非表示時間
 * @param onClose 閉じるイベントハンドラ
 * @returns {JSX.Element} JSX.Element
 */
const Alertbar = ({
  open,
  message,
  severity,
  autoHideDuration = null,
  onClose,
}: Props): JSX.Element => (
  <Snackbar
    sx={{ width: '400px' }}
    anchorOrigin={{ vertical: 'top', horizontal: 'center' }}
    open={open}
    autoHideDuration={autoHideDuration}
    onClose={onClose}
  >
    <Alert sx={{ width: '100%' }} severity={severity} onClose={onClose}>
      {message}
    </Alert>
  </Snackbar>
);
export default Alertbar;
