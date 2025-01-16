/**
 * サイドメニュー モジュールコンポーネント
 * Copyright (C) ITS Corporation. All Rights Reserved.
 */
import { JSX, ReactNode, useState, useContext, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';

import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';
import PersonOutlinedIcon from '@mui/icons-material/PersonOutlined';
import {
  Drawer,
  Box,
  AppBar,
  Toolbar,
  Card,
  CardMedia,
  IconButton,
  List,
  ListItemIcon,
  ListItemText,
  ListSubheader,
  ListItemButton,
  Collapse,
} from '@mui/material';
// import { styled } from '@mui/material/styles';
// import {
//   STYLE,
//   SUB_MENU_NAME,
//   SubMenuType,
//   PAGE_NAME,
//   PageNameType,
//   PAGE_LINK,
//   AUTH_CLS_CD,
// } from '@config/appConsts';
// import AcceptOrderEditor, {
//   AcceptOrderEditorOpenState,
// } from 'components/pages/transaction/acceptOrder/AcceptOrderEditor';
// import { AuthContext } from 'contexts/AuthContext';
// import { useSetRecoilState } from 'recoil';

import { IPageLinkType } from '@/common/config/types';
import { ISideMenu } from '@/common/components/ISideMenu';

/** ドロワー幅 */
export const DRAWER_WIDTH = 250 as const;

// export interface ISideMenuChildren {
//   getSiderMenuChildren(): JSX.Element;
// }

type Props = {
  // selectedSubMenu?: SubMenuType | null;
  // selectedPage?: PageNameType | null;
  homePageLink: IPageLinkType;
  sideMenuOpen: boolean;
  setSideMenuOpen: React.Dispatch<React.SetStateAction<boolean>>;
  children?: ReactNode;
};

/**
 * サイドメニュー
 * @param Props.selectedSubMenu 選択中サブメニュー
 * @param Props.selectedPageCd 選択中ページ
 * @param Props.sideMenuOpen サイドメニュー開閉フラグ
 * @param Props.setSideMenuOpen サイドメニュー開閉フラグ設定用関数
 * @returns {JSX.Element} JSX.Element
 */
const SideMenu = ({
  // selectedSubMenu = null,
  // selectedPage = null,
  homePageLink,
  sideMenuOpen,
  setSideMenuOpen,
  children,
}: Props): JSX.Element => {
  // // ListItemスタイル
  // const StyListItem = styled('div')({
  //   borderBottom: '1px solid #d8d8d8',
  // });

  // // ListItemButtonスタイル
  // const StyListItemButton = styled(ListItemButton)(() => ({
  //   paddingTop: 15,
  //   paddingBottom: 15,
  // }));

  // // サブListItemButtonスタイル
  // const StySubListItemButton = styled(ListItemButton)(() => ({
  //   paddingLeft: 40,
  //   '&.Mui-selected': {
  //     background: '#98cfff',
  //   },
  // }));

  // // Linkスタイル
  // const StyLink = styled(Link)(() => ({
  //   color: STYLE.BASE_COLOR,
  //   textDecoration: 'none',
  // }));

  // // 認証情報
  // const { auth, setAuth } = useContext(AuthContext);
  // メニューアイテム開閉フラグ
  const [menuItemOpens, setMenuItemOpens] = useState({
    user: false,
    order: false,
    shipping: false,
    rental: false,
    return: false,
    master: false,
  });
  // メニューアイテムフル開閉フラグ
  const [menuItemFullOpen, setMenuItemFullOpen] = useState(false);
  // 画面遷移用関数
  const navigate = useNavigate();

  /**
   * 選択中サブメニューを展開する
   */
  // useEffect(() => {
  //   if (!selectedSubMenu) return;
  //   switch (selectedSubMenu) {
  //     case SUB_MENU_NAME.ACCEPT_ORDER:
  //       setMenuItemOpens({ ...menuItemOpens, order: true });
  //       break;
  //     case SUB_MENU_NAME.SHIPPING:
  //       setMenuItemOpens({ ...menuItemOpens, shipping: true });
  //       break;
  //     case SUB_MENU_NAME.RENTAL:
  //       setMenuItemOpens({ ...menuItemOpens, rental: true });
  //       break;
  //     case SUB_MENU_NAME.BACK:
  //       setMenuItemOpens({ ...menuItemOpens, return: true });
  //       break;
  //     case SUB_MENU_NAME.MASTER:
  //       setMenuItemOpens({ ...menuItemOpens, master: true });
  //       break;
  //     default:
  //       break;
  //   }
  // }, [menuItemOpens, selectedSubMenu]);

  /**
   * [メニュー]クリックイベントハンドラ
   */
  // const handleMenuClick = () => {
  //   const menuItemOpenValues = Object.values(menuItemOpens);

  //   // 一つ以上閉じていたらすべて開く
  //   if (menuItemOpenValues.some(value => !value)) {
  //     setMenuItemOpens({
  //       user: true,
  //       order: true,
  //       shipping: true,
  //       rental: true,
  //       return: true,
  //       master: true,
  //     });
  //     setMenuItemFullOpen(true);
  //     return;
  //   }

  //   // すべて開いていたらすべて閉じる
  //   if (!menuItemOpenValues.some(value => !value)) {
  //     setMenuItemOpens({
  //       user: false,
  //       order: false,
  //       shipping: false,
  //       rental: false,
  //       return: false,
  //       master: false,
  //     });
  //     setMenuItemFullOpen(false);
  //     return;
  //   }

  //   setMenuItemOpens({
  //     user: !menuItemFullOpen,
  //     order: !menuItemFullOpen,
  //     shipping: !menuItemFullOpen,
  //     rental: !menuItemFullOpen,
  //     return: !menuItemFullOpen,
  //     master: !menuItemFullOpen,
  //   });
  //   setMenuItemFullOpen(!menuItemFullOpen);
  // };

  /**
   * ログアウトイベントハンドラ
   */
  // const handleLogout = () => {
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

  return (
    <Drawer
      sx={{
        width: sideMenuOpen ? DRAWER_WIDTH : 0,
        height: '100vh',
        overflowY: 'scroll',
        flexShrink: 0,
        transition: theme =>
          theme.transitions.create(['margin', 'width'], {
            easing: sideMenuOpen
              ? theme.transitions.easing.sharp
              : theme.transitions.easing.easeOut,
            duration: sideMenuOpen
              ? theme.transitions.duration.leavingScreen
              : theme.transitions.duration.enteringScreen,
          }),
        '& .MuiDrawer-paper': {
          width: DRAWER_WIDTH,
          boxSizing: 'border-box',
        },
      }}
      variant="persistent"
      anchor="left"
      open={sideMenuOpen}
    >
      <List
        component="nav"
        aria-labelledby="menu"
        subheader={
          <Box>
            <AppBar position="static" color="inherit">
              <Toolbar style={{ padding: 0, display: 'flex' }}>
                <Link data-testid="linkMainMenu" to={homePageLink}>
                  <Card sx={{ boxShadow: 'none', pt: 2, mb: 2 }}>
                    <CardMedia
                      sx={{ display: 'block', width: 150, ml: 1 }}
                      component="img"
                      image="/assets/images/logo_s.png"
                    />
                  </Card>
                </Link>
                {/* <Box sx={{ ml: 'auto' }}>
                  {selectedPage && (
                    <IconButton onClick={() => setSideMenuOpen(false)}>
                      <ChevronLeftIcon />
                    </IconButton>
                  )}
                </Box> */}
              </Toolbar>
            </AppBar>
            <ListSubheader
              sx={{ cursor: 'pointer', color: '#1b1b1b' }}
              component="div"
              id="menu"
              // onClick={handleMenuClick}
            >
              メニュー
            </ListSubheader>
          </Box>
        }
      >
        {children}
      </List>
    </Drawer>
  );
};
export default SideMenu;
