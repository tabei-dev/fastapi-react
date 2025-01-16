/**
 * サイドメニュー モジュールコンポーネント
 * Copyright (C) ITS Corporation. All Rights Reserved.
 */
import { JSX, useState, useContext, useEffect } from 'react';
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
import { styled } from '@mui/material/styles';
import {
  STYLE,
  SUB_MENU_NAME,
  SubMenuType,
  PAGE_NAME,
  PageNameType,
  PAGE_LINK,
  AUTH_CLS_CD,
} from '@config/appConsts';
// import AcceptOrderEditor, {
//   AcceptOrderEditorOpenState,
// } from 'components/pages/transaction/acceptOrder/AcceptOrderEditor';
import { AuthContext } from 'contexts/AuthContext';
import { useSetRecoilState } from 'recoil';

/** ドロワー幅 */
export const DRAWER_WIDTH = 250 as const;

type Props = {
  selectedSubMenu?: SubMenuType | null;
  selectedPage?: PageNameType | null;
  sideMenuOpen: boolean;
  setSideMenuOpen: React.Dispatch<React.SetStateAction<boolean>>;
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
  selectedSubMenu = null,
  selectedPage = null,
  sideMenuOpen,
  setSideMenuOpen,
}: Props): JSX.Element => {
  // ListItemスタイル
  const StyListItem = styled('div')({
    borderBottom: '1px solid #d8d8d8',
  });

  // ListItemButtonスタイル
  const StyListItemButton = styled(ListItemButton)(() => ({
    paddingTop: 15,
    paddingBottom: 15,
  }));

  // サブListItemButtonスタイル
  const StySubListItemButton = styled(ListItemButton)(() => ({
    paddingLeft: 40,
    '&.Mui-selected': {
      background: '#98cfff',
    },
  }));

  // Linkスタイル
  const StyLink = styled(Link)(() => ({
    color: STYLE.BASE_COLOR,
    textDecoration: 'none',
  }));

  // 認証情報
  const { auth, setAuth } = useContext(AuthContext);
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
  useEffect(() => {
    if (!selectedSubMenu) return;
    switch (selectedSubMenu) {
      case SUB_MENU_NAME.ACCEPT_ORDER:
        setMenuItemOpens({ ...menuItemOpens, order: true });
        break;
      case SUB_MENU_NAME.SHIPPING:
        setMenuItemOpens({ ...menuItemOpens, shipping: true });
        break;
      case SUB_MENU_NAME.RENTAL:
        setMenuItemOpens({ ...menuItemOpens, rental: true });
        break;
      case SUB_MENU_NAME.BACK:
        setMenuItemOpens({ ...menuItemOpens, return: true });
        break;
      case SUB_MENU_NAME.MASTER:
        setMenuItemOpens({ ...menuItemOpens, master: true });
        break;
      default:
        break;
    }
  }, [menuItemOpens, selectedSubMenu]);

  /**
   * [メニュー]クリックイベントハンドラ
   */
  const handleMenuClick = () => {
    const menuItemOpenValues = Object.values(menuItemOpens);

    // 一つ以上閉じていたらすべて開く
    if (menuItemOpenValues.some(value => !value)) {
      setMenuItemOpens({
        user: true,
        order: true,
        shipping: true,
        rental: true,
        return: true,
        master: true,
      });
      setMenuItemFullOpen(true);
      return;
    }

    // すべて開いていたらすべて閉じる
    if (!menuItemOpenValues.some(value => !value)) {
      setMenuItemOpens({
        user: false,
        order: false,
        shipping: false,
        rental: false,
        return: false,
        master: false,
      });
      setMenuItemFullOpen(false);
      return;
    }

    setMenuItemOpens({
      user: !menuItemFullOpen,
      order: !menuItemFullOpen,
      shipping: !menuItemFullOpen,
      rental: !menuItemFullOpen,
      return: !menuItemFullOpen,
      master: !menuItemFullOpen,
    });
    setMenuItemFullOpen(!menuItemFullOpen);
  };

  /**
   * [ユーザー]クリックイベントハンドラ
   */
  const handleUserClick = () => {
    setMenuItemOpens({ ...menuItemOpens, user: !menuItemOpens.user });
  };

  /**
   * [受注管理]クリックイベントハンドラ
   */
  const handleOrdersClick = () => {
    setMenuItemOpens({ ...menuItemOpens, order: !menuItemOpens.order });
  };

  /**
   * [出荷管理]クリックイベントハンドラ
   */
  const handleShippingClick = () => {
    setMenuItemOpens({ ...menuItemOpens, shipping: !menuItemOpens.shipping });
  };

  /**
   * [貸出管理]クリックイベントハンドラ
   */
  const handleRentalClick = () => {
    setMenuItemOpens({ ...menuItemOpens, rental: !menuItemOpens.rental });
  };

  /**
   * [帰着管理]クリックイベントハンドラ
   */
  const handleReturnClick = () => {
    setMenuItemOpens({ ...menuItemOpens, return: !menuItemOpens.return });
  };

  /**
   * [マスタ管理]クリックイベントハンドラ
   */
  const handleMasterClick = () => {
    setMenuItemOpens({ ...menuItemOpens, master: !menuItemOpens.master });
  };

  // 注文データ登録画面表示フラグ（セッターのみ）
  const setAcceptOrderEditorOpen = useSetRecoilState(
    AcceptOrderEditorOpenState,
  );

  /**
   * ログアウトイベントハンドラ
   */
  const handleLogout = () => {
    // 認証情報をクリアしてログアウト
    setAuth({
      userId: '',
      loginId: '',
      userName: '',
      authClsCd: '',
      companyId: '',
    });
    // ホーム画面に遷移
    navigate('/');
  };

  return (
    <Drawer
      sx={{
        width: sideMenuOpen ? DRAWER_WIDTH : 0,
        height: '100vh',
        overflowY: 'scroll',
        flexShrink: 0,
        transition: (theme) =>
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
                <Link
                  data-testid="linkMainMenu"
                  to={PAGE_LINK.ACCEPT_ORDER_REFERENCE}
                >
                  <Card sx={{ boxShadow: 'none', pt: 2, mb: 2 }}>
                    <CardMedia
                      sx={{ display: 'block', width: 150, ml: 1 }}
                      component="img"
                      image="/assets/images/logo_s_main.png"
                      // title="logo"
                    />
                  </Card>
                </Link>
                <Box sx={{ ml: 'auto' }}>
                  {selectedPage && (
                    <IconButton onClick={() => setSideMenuOpen(false)}>
                      <ChevronLeftIcon />
                    </IconButton>
                  )}
                </Box>
              </Toolbar>
            </AppBar>
            <ListSubheader
              sx={{ cursor: 'pointer', color: '#1b1b1b' }}
              component="div"
              id="menu"
              onClick={handleMenuClick}
            >
              メニュー
            </ListSubheader>
          </Box>
        }
      >
        {/*
          ユーザー
        */}
        <StyListItem>
          <StyListItemButton onClick={handleUserClick}>
            <ListItemIcon>
              <PersonOutlinedIcon />
            </ListItemIcon>
            <ListItemText primary={`${auth.userName} さん`} />
            {menuItemOpens.user ? <ExpandLess /> : <ExpandMore />}
          </StyListItemButton>
          <Collapse in={menuItemOpens.user} timeout="auto" unmountOnExit>
            <List component="div" disablePadding>
              <StySubListItemButton onClick={handleLogout}>
                <ListItemText primary="ログアウト" />
              </StySubListItemButton>
            </List>
          </Collapse>
        </StyListItem>
        {/*
          受注管理
        */}
        {(auth.authClsCd === AUTH_CLS_CD.ADMINISTRATOR ||
          auth.authClsCd === AUTH_CLS_CD.GENERAL_STAFF) && (
          <StyListItem>
            <StyListItemButton onClick={handleOrdersClick}>
              <ListItemText primary="受注管理" />
              {menuItemOpens.order ? <ExpandLess /> : <ExpandMore />}
            </StyListItemButton>
            <Collapse in={menuItemOpens.order} timeout="auto" unmountOnExit>
              <List component="div" disablePadding>
                {/*
                  注文データ登録
                */}
                <StySubListItemButton
                  onClick={() => setAcceptOrderEditorOpen(true)}
                >
                  <ListItemText
                    primary={PAGE_NAME.ACCEPT_ORDER_EDITOR.toString()}
                  />
                </StySubListItemButton>
                {/*
                  注文データ照会
                */}
                <StyLink to={PAGE_LINK.ACCEPT_ORDER_REFERENCE.toString()}>
                  <StySubListItemButton
                    selected={selectedPage === PAGE_NAME.ACCEPT_ORDER_REFERENCE}
                  >
                    <ListItemText
                      primary={PAGE_NAME.ACCEPT_ORDER_REFERENCE.toString()}
                    />
                  </StySubListItemButton>
                </StyLink>
              </List>
            </Collapse>
          </StyListItem>
        )}
        {/*
          出荷管理
        */}
        {(auth.authClsCd === AUTH_CLS_CD.ADMINISTRATOR ||
          auth.authClsCd === AUTH_CLS_CD.GENERAL_STAFF ||
          auth.authClsCd === AUTH_CLS_CD.SHIP_STAFF) && (
          <StyListItem>
            <StyListItemButton onClick={handleShippingClick}>
              <ListItemText primary="出荷管理" />
              {menuItemOpens.shipping ? <ExpandLess /> : <ExpandMore />}
            </StyListItemButton>
            <Collapse in={menuItemOpens.shipping} timeout="auto" unmountOnExit>
              <List component="div" disablePadding>
                {/*
                  出荷予定照会
                */}
                <StyLink to={PAGE_LINK.SHIP_EXP_REFERENCE.toString()}>
                  <StySubListItemButton
                    selected={selectedPage === PAGE_NAME.SHIP_EXP_REFERENCE}
                  >
                    <ListItemText
                      primary={PAGE_NAME.SHIP_EXP_REFERENCE.toString()}
                    />
                  </StySubListItemButton>
                </StyLink>
                {/*
                  出荷実績照会
                */}
                <StyLink to={PAGE_LINK.SHIP_RESULT_REFERENCE.toString()}>
                  <StySubListItemButton
                    selected={selectedPage === PAGE_NAME.SHIP_RESULT_REFERENCE}
                  >
                    <ListItemText
                      primary={PAGE_NAME.SHIP_RESULT_REFERENCE.toString()}
                    />
                  </StySubListItemButton>
                </StyLink>
              </List>
            </Collapse>
          </StyListItem>
        )}
        {/*
          貸出管理
        */}
        {(auth.authClsCd === AUTH_CLS_CD.ADMINISTRATOR ||
          auth.authClsCd === AUTH_CLS_CD.GENERAL_STAFF ||
          auth.authClsCd === AUTH_CLS_CD.CUSTOMER_STAFF) && (
          <StyListItem>
            <StyListItemButton onClick={handleRentalClick}>
              <ListItemText primary="貸出管理" />
              {menuItemOpens.rental ? <ExpandLess /> : <ExpandMore />}
            </StyListItemButton>
            <Collapse in={menuItemOpens.rental} timeout="auto" unmountOnExit>
              <List component="div" disablePadding>
                {/*
                  貸出容器照会
                */}
                <StyLink to={PAGE_LINK.RENTAL_BOMBE_REFERENCE.toString()}>
                  <StySubListItemButton
                    selected={selectedPage === PAGE_NAME.RENTAL_BOMBE_REFERENCE}
                  >
                    <ListItemText
                      primary={PAGE_NAME.RENTAL_BOMBE_REFERENCE.toString()}
                    />
                  </StySubListItemButton>
                </StyLink>
                {/*
                  容器得意先台帳出力
                */}
                <StyLink to={PAGE_LINK.BOMBE_CUSTOMER_LEDGER_OUT.toString()}>
                  <StySubListItemButton
                    selected={
                      selectedPage === PAGE_NAME.BOMBE_CUSTOMER_LEDGER_OUT
                    }
                  >
                    <ListItemText
                      primary={PAGE_NAME.BOMBE_CUSTOMER_LEDGER_OUT.toString()}
                    />
                  </StySubListItemButton>
                </StyLink>
              </List>
            </Collapse>
          </StyListItem>
        )}
        {/*
          帰着管理
        */}
        {(auth.authClsCd === AUTH_CLS_CD.ADMINISTRATOR ||
          auth.authClsCd === AUTH_CLS_CD.GENERAL_STAFF) && (
          <StyListItem>
            <StyListItemButton onClick={handleReturnClick}>
              <ListItemText primary="帰着管理" />
              {menuItemOpens.return ? <ExpandLess /> : <ExpandMore />}
            </StyListItemButton>
            <Collapse in={menuItemOpens.return} timeout="auto" unmountOnExit>
              <List component="div" disablePadding>
                {/*
                  帰着容器登録
                */}
                <StyLink to={PAGE_LINK.BACK_BOMBE_EDITOR.toString()}>
                  <StySubListItemButton
                    selected={selectedPage === PAGE_NAME.BACK_BOMBE_EDITOR}
                  >
                    <ListItemText
                      primary={PAGE_NAME.BACK_BOMBE_EDITOR.toString()}
                    />
                  </StySubListItemButton>
                </StyLink>
              </List>
            </Collapse>
          </StyListItem>
        )}
        {/*
          マスタ管理
        */}
        {auth.authClsCd === AUTH_CLS_CD.ADMINISTRATOR && (
          <StyListItem>
            <StyListItemButton onClick={handleMasterClick}>
              <ListItemText primary="マスタ管理" />
              {menuItemOpens.master ? <ExpandLess /> : <ExpandMore />}
            </StyListItemButton>
            <Collapse in={menuItemOpens.master} timeout="auto" unmountOnExit>
              <List component="div" disablePadding>
                {/*
                  ユーザーマスタ照会
                */}
                <StyLink to={PAGE_LINK.USER_MASTER_REFERENCE.toString()}>
                  <StySubListItemButton
                    selected={selectedPage === PAGE_NAME.USER_MASTER_REFERENCE}
                  >
                    <ListItemText
                      primary={PAGE_NAME.USER_MASTER_REFERENCE.toString()}
                    />
                  </StySubListItemButton>
                </StyLink>
                {/*
                  会社マスタ照会
                */}
                <StyLink to={PAGE_LINK.COMPANY_MASTER_REFERENCE.toString()}>
                  <StySubListItemButton
                    selected={
                      selectedPage === PAGE_NAME.COMPANY_MASTER_REFERENCE
                    }
                  >
                    <ListItemText
                      primary={PAGE_NAME.COMPANY_MASTER_REFERENCE.toString()}
                    />
                  </StySubListItemButton>
                </StyLink>
                {/*
                  直送先マスタ照会
                */}
                <StyLink to={PAGE_LINK.DELIV_DEST_MASTER_REFERENCE.toString()}>
                  <StySubListItemButton
                    selected={
                      selectedPage === PAGE_NAME.DELIV_DEST_MASTER_REFERENCE
                    }
                  >
                    <ListItemText
                      primary={PAGE_NAME.DELIV_DEST_MASTER_REFERENCE.toString()}
                    />
                  </StySubListItemButton>
                </StyLink>
                {/*
                  容器管理者マスタ照会
                */}
                <StyLink to={PAGE_LINK.BOMBE_MNG_MASTER_REFERENCE.toString()}>
                  <StySubListItemButton
                    selected={
                      selectedPage === PAGE_NAME.BOMBE_MNG_MASTER_REFERENCE
                    }
                  >
                    <ListItemText
                      primary={PAGE_NAME.BOMBE_MNG_MASTER_REFERENCE.toString()}
                    />
                  </StySubListItemButton>
                </StyLink>
                {/*
                  商品マスタ照会
                */}
                <StyLink to={PAGE_LINK.PRODUCT_MASTER_REFERENCE.toString()}>
                  <StySubListItemButton
                    selected={
                      selectedPage === PAGE_NAME.PRODUCT_MASTER_REFERENCE
                    }
                  >
                    <ListItemText
                      primary={PAGE_NAME.PRODUCT_MASTER_REFERENCE.toString()}
                    />
                  </StySubListItemButton>
                </StyLink>

                {/*
                  容器マスタ照会
                */}
                <StyLink to={PAGE_LINK.BOMBE_MASTER_REFERENCE.toString()}>
                  <StySubListItemButton
                    selected={selectedPage === PAGE_NAME.BOMBE_MASTER_REFERENCE}
                  >
                    <ListItemText
                      primary={PAGE_NAME.BOMBE_MASTER_REFERENCE.toString()}
                    />
                  </StySubListItemButton>
                </StyLink>
              </List>
            </Collapse>
          </StyListItem>
        )}
      </List>
      {/* 注文データ登録モーダル画面 */}
      <AcceptOrderEditor />
    </Drawer>
  );
};
export default SideMenu;
