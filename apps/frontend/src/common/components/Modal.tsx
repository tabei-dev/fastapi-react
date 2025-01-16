/**
 * モーダル用モジュールコンポーネント
 * Copyright (C) ITS Corporation. All Rights Reserved.
 */
import { JSX, ReactNode, useEffect } from 'react';

import HighlightOffRoundedIcon from '@mui/icons-material/HighlightOffRounded';
import { Stack, Box } from '@mui/material';
import { atom, useRecoilState } from 'recoil';

import { AlertInfo } from '@/common/components/Alertbar';
import { PageNameType } from '@/common/config/consts';

/**
 * 表示中モーダル一覧
 * @type {RecoilState<Map<PageNameType, React.Dispatch<React.SetStateAction<boolean>>>}
 * @default new Map()
 * @see https://recoiljs.org/docs/api-reference/core/atom
 * @see https://recoiljs.org/docs/api-reference/core/useRecoilState
 */
export const OpenModalList = atom<Map<PageNameType, React.Dispatch<React.SetStateAction<boolean>>>>(
  {
    key: 'OpenModalList',
    default: new Map(),
  }
);

/**
 * モーダルウィンドウのヘッダー部 モジュールコンポーネント用プロパティ
 * @param pageName ページ名
 * @param setOpen モーダルウィンドウ表示フラグ設定用関数
 * @param setAlert アラート設定用関数
 */
type ModalHeaderProps = {
  pageName: PageNameType;
  setOpen: React.Dispatch<React.SetStateAction<boolean>>;
  setAlert?: React.Dispatch<React.SetStateAction<AlertInfo>> | null;
};

/**
 * モーダルウィンドウのヘッダー部 モジュールコンポーネント
 * @param pageName ページ名
 * @param setOpen モーダルウィンドウ表示フラグ設定用関数
 * @param setAlert アラート設定用関数
 * @returns {JSX.Element} JSX.Element
 */
export const ModalHeader = ({
  pageName,
  setOpen,
  setAlert = null,
}: ModalHeaderProps): JSX.Element => {
  // 表示中モーダル一覧
  const [openModalList, setOpenModalList] = useRecoilState(OpenModalList);

  /**
   * 指定のモーダル画面を一覧に追加します。
   */
  useEffect(() => {
    openModalList.set(pageName, setOpen);
    setOpenModalList(openModalList);
  }, [openModalList, pageName, setOpen, setOpenModalList]);

  return (
    <Stack direction="row" sx={{ alignItems: 'center', m: 1, p: 1 }}>
      {/* ページ名 */}
      <Box sx={{ fontWeight: 'bold' }}>{pageName.toString()}</Box>
      {/* 閉じるボタン */}
      <HighlightOffRoundedIcon
        sx={{
          fontSize: 36,
          ml: 'auto',
          mb: 2,
          '&:hover': {
            cursor: 'pointer',
          },
        }}
        onClick={() => {
          setAlert?.({ open: false, message: '', severity: 'success' });
          setOpen(false);
        }}
      />
    </Stack>
  );
};

type ModalMainProps = {
  children: ReactNode;
};

/**
 * モーダルウィンドウのメイン部 モジュールコンポーネント
 * @param children 子ノード
 * @returns {JSX.Element} JSX.Element
 */
export const ModalMain = ({ children }: ModalMainProps): JSX.Element => (
  <Stack spacing={2} sx={{ m: 1, px: 2, pt: 1, pb: 2 }}>
    {children}
  </Stack>
);

type ModalFooterProps = {
  children: ReactNode;
};

/**
 * モーダルウィンドウのフッター部 モジュールコンポーネント
 * @param children 子ノード
 * @returns {JSX.Element} JSX.Element
 */
export const ModalFooter = ({ children }: ModalFooterProps): JSX.Element => (
  <Stack direction="row" spacing={2} sx={{ justifyContent: 'center', m: 1, p: 2 }}>
    {children}
  </Stack>
);
