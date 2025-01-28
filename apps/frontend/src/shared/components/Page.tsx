/**
 * ページ モジュールコンポーネント
 */
import { JSX, ReactNode, useState } from 'react';
// import { useNavigate } from 'react-router-dom';

import { Box } from '@mui/material';

import Breadcrumb from '@/shared/components/Breadcrumb';
// import { OpenModalList } from '@/shared/components/Modal';
import SideMenu, { DRAWER_WIDTH } from '@/shared/components/SideMenu';

type Props = {
  children: ReactNode;
};

/**
 * ページ
 * @param children 子ノード
 * @returns {JSX.Element} JSX.Element
 */
const Page = ({ children }: Props): JSX.Element => {
  const [sideMenuOpen, setSideMenuOpen] = useState(true);
  // const [alert, setAlert] = useState({ open: false, message: '' });
  // const navigate = useNavigate();

  return (
    <Box sx={{ display: 'flex' }}>
      {/* サイドメニュー */}
      <SideMenu sideMenuOpen={sideMenuOpen} setSideMenuOpen={setSideMenuOpen} />
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
        <Breadcrumb sideMenuOpen={sideMenuOpen} setSideMenuOpen={setSideMenuOpen} />
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
