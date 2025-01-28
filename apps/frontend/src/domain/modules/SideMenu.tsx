import { JSX, useState } from 'react';
import { useNavigate } from 'react-router-dom';

import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';
import PersonOutlinedIcon from '@mui/icons-material/PersonOutlined';
import { ListSubheader, ListItemIcon, ListItemText, Collapse, List } from '@mui/material';

import { PAGE_LINKS } from '@/domain/config/consts';
import authAPI from '@/domain/services/authService';
import { ISideMenu } from '@/shared/components/ISideMenu';
import { ListItemStyle, ListItemButtonStyle } from '@/shared/styles/sideMenu';

const SideMenuChildren = (): JSX.Element => {
  // 画面遷移用関数
  const navigate = useNavigate();
  // const handleUserClick = () => {
  //   setMenuItemOpens({
  //     ...menuItemOpens,
  //     user: !menuItemOpens.user,
  //   });
  // };

  type Category = 'user' | 'master';
  const categories: Category[] = ['user', 'master'] as const;

  // const [menuItemOpens, setMenuItemOpens] = useState(
  //   new Map<string, boolean>([
  //     ['user', false],
  //     ['master', false],
  //   ])
  // );

  /**
   * メニューアイテム開閉フラグリストを生成します。
   * @param open 開閉フラグ
   * @returns メニューアイテム開閉フラグリスト
   */
  const createMenuItemOpens = (open: boolean) => {
    const obj: { [key: string]: boolean } = {};
    categories.forEach(category => {
      obj[category] = open;
    });
    return obj;
  };

  // メニューアイテム開閉フラグリスト
  const [menuItemOpens, setMenuItemOpens] = useState(createMenuItemOpens(false));

  /**
   * [メニュー] クリックイベントハンドラ
   * @returns
   */
  const handleMenuClick = () => {
    const menuItemOpenValues = Object.values(menuItemOpens);

    // カテゴリが一つ以上閉じていたらすべて開く
    if (menuItemOpenValues.some(value => !value)) {
      setMenuItemOpens(createMenuItemOpens(true));
      return;
    }
    // カテゴリがすべて開いていたらすべて閉じる
    if (!menuItemOpenValues.some(value => !value)) {
      setMenuItemOpens(createMenuItemOpens(false));
      return;
    }
  };

  /**
   * リストアイテムボタンクリックイベントハンドラ
   * @param category カテゴリ
   */
  const handleListItemButtonClick = (category: Category) => {
    // 指定カテゴリの開閉状態を反転
    setMenuItemOpens({ ...menuItemOpens, [category]: !menuItemOpens[category] });
  };

  /**
   * ログアウトボタンクリックイベントハンドラ
   */
  const handleLogoutClick = () => {
    authAPI.logout();
    navigate('/');
  };

  return (
    <>
      <ListSubheader
        sx={{ cursor: 'pointer', color: '#1b1b1b' }}
        component="div"
        id="menu"
        onClick={handleMenuClick}
      >
        メニュー
      </ListSubheader>
      {/*
        ユーザー
      */}
      <ListItemStyle>
        <ListItemButtonStyle onClick={() => handleListItemButtonClick('user')}>
          <ListItemIcon>
            <PersonOutlinedIcon />
          </ListItemIcon>
          <ListItemText primary={`${authAPI.getAuth().username} さん`} />
          {menuItemOpens.user ? <ExpandLess /> : <ExpandMore />}
        </ListItemButtonStyle>
        <Collapse in={menuItemOpens.user} timeout="auto" unmountOnExit>
          <List component="div" disablePadding>
            <ListItemButtonStyle onClick={handleLogoutClick}>
              <ListItemText primary="ログアウト" />
            </ListItemButtonStyle>
          </List>
        </Collapse>
      </ListItemStyle>
    </>
  );
};

class SideMenu implements ISideMenu {
  /**
   * ホームページリンクを取得します。
   * @returns {string} ホームページリンク
   */
  getHopePageLink(): string {
    return PAGE_LINKS.MENU;
  }

  /**
   * ホームページリンクを取得します。
   * @returns {string} ホームページリンク
   */
  getSiderMenuChildren(): JSX.Element {
    return <SideMenuChildren />;
  }
}
export default SideMenu;
