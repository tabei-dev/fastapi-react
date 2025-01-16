/**
 * ページ モジュールコンポーネント
 */
import { JSX, ReactNode, useContext, useState, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
// import { useKey, useEvent } from 'react-use';

import { Box } from '@mui/material';
// import { AuthContext } from 'contexts/AuthContext';
import { useRecoilValue } from 'recoil';

// import Alertbar from '@/common/components/Alertbar';
import Breadcrumb from '@/common/components/Breadcrumb';
import { OpenModalList } from '@/common/components/Modal';
import SideMenu, { DRAWER_WIDTH } from '@/common/components/SideMenu';
// import { ICategoryType, IPageType } from '@/common/config/types';

type Props = {
  // category?: ICategoryType | null;
  // page?: IPageType | null;
  category?: string | undefined;
  page?: string | undefined;
  children: ReactNode;
};

/**
 * ページ
 * @param Props.subMenu サブメニュー
 * @param Props.page ページ
 * @param Props.children 子ノード
 * @returns {JSX.Element} JSX.Element
 */
const Page = ({ category = undefined, page = undefined, children }: Props): JSX.Element => {
  // 認証情報
  // const { setAuth, lastTime, setLastTime } = useContext(AuthContext);
  // サイドメニュー開閉フラグ
  const [sideMenuOpen, setSideMenuOpen] = useState(true);
  // アラート情報
  const [alert, setAlert] = useState({ open: false, message: '' });
  // 画面遷移用関数
  const navigate = useNavigate();
  // // 表示中モーダル一覧
  // const openModalList = useRecoilValue(OpenModalList);

  /**
   * タイムアウトかどうかを判定
   */
  // const ditectTimeout = () => {
  //   // 現在時刻より最終操作時刻を減じた値（ミリ秒）が.envのVITE_LIFETIME（分）を
  //   // 超えている場合はタイムアウトとしてAlertbarを出力
  //   if (Date.now() - lastTime > import.meta.env.VITE_LIFETIME * 60 * 1000) {
  //     setAlert({
  //       open: true,
  //       message: '一定時間操作がなかったためログアウトします。',
  //     });
  //   }
  //   // 最終操作時刻を再設定
  //   setLastTime(Date.now());
  // };

  /**
   * Alertbarクローズイベントハンドラ
   */
  // const handleAlertberClose = () => {
  //   // アラートを消去
  //   setAlert({ open: false, message: '' });
  //   // 表示中のモーダル画面をすべて閉じる
  //   openModalList.forEach(openModal => openModal(false));
  //   // 認証情報をクリアしてログアウト
  //   setAuth({
  //     userId: '',
  //     loginId: '',
  //     userName: '',
  //     authClsCd: '',
  //     companyId: '',
  //   });
  //   // ホーム画面に遷移
  //   navigate('/');
  // };

  // // F5とCtrl+rを無効化
  // useKey(
  //   (e: { key: string; ctrlKey: any }) =>
  //     e.key === 'F5' || (e.ctrlKey && e.key === 'r'),
  //   (e: Event) => e.preventDefault(),
  //   { event: 'keydown' },
  // );

  // // ブラウザの更新ボタンが押されたときにalertを出力する
  // useEvent(
  //   'beforeunload',
  //   useCallback((e: BeforeUnloadEvent) => {
  //     e.preventDefault();
  //     e.returnValue = '';
  //   }, []),
  // );

  return (
    // <Box sx={{ display: 'flex' }} onClick={ditectTimeout}>
    <Box sx={{ display: 'flex' }}>
      {/* サイドメニュー */}
      <SideMenu
        selectedSubMenu={category}
        // homePageLink={category}
        selectedPage={page}
        sideMenuOpen={sideMenuOpen}
        setSideMenuOpen={setSideMenuOpen}
      />
      <Box
        sx={{
          width: sideMenuOpen ? `calc(100vw - ${DRAWER_WIDTH}px)` : '100vw',
          height: '100vh',
          bgcolor: '#ececec',
          overflow: 'hidden',
          transition: theme =>
            theme.transitions.create(['margin', 'width'], {
              easing: sideMenuOpen
                ? theme.transitions.easing.easeOut
                : theme.transitions.easing.sharp,
              duration: sideMenuOpen
                ? theme.transitions.duration.enteringScreen
                : theme.transitions.duration.leavingScreen,
            }),
        }}
      >
        {/* パンくずリスト */}
        <Breadcrumb
          category={category}
          page={page}
          sideMenuOpen={sideMenuOpen}
          setSideMenuOpen={setSideMenuOpen}
        />
        {/* メインコンテンツ */}
        {children}
      </Box>
      {/* <Alertbar
        open={alert.open}
        message={alert.message}
        severity="error"
        autoHideDuration={6000}
        onClose={handleAlertberClose}
      /> */}
    </Box>
  );
};
export default Page;
