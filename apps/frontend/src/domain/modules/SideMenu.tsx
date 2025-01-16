import { JSX, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom'

import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';
import PersonOutlinedIcon from '@mui/icons-material/PersonOutlined';
import { ListItemIcon, ListItemText, Collapse, List } from '@mui/material';

import { ISideMenu } from '@/common/components/ISideMenu';
import { ListItemStyle, ListItemButtonStyle } from '@/common/styles/sideMenu';
import { PAGE_LINKS } from '@/domain/config/consts';

const SideMenu = (): JSX.Element => {
  // 画面遷移用関数
  const navigate = useNavigate();
  // const handleUserClick = () => {
  //   setMenuItemOpens({
  //     ...menuItemOpens,
  //     user: !menuItemOpens.user,
  //   });
  // };

  const [menuItemOpens, setMenuItemOpens] = useState(
    new Map<string, boolean>([
      ['user', false],
      ['master', false],
    ])
  );

  const handleLogout = () => {
    // setAuth({ ...auth, isLogin: false });
    navigate('/');
  };

  return (
    <>
      {/*
        ユーザー
      */}
      <ListItemStyle>
        <ListItemButtonStyle onClick={handleUserClick}>
          <ListItemIcon>
            <PersonOutlinedIcon />
          </ListItemIcon>
          <ListItemText primary={`${auth.userName} さん`} />
          {menuItemOpens.get('user') ? <ExpandLess /> : <ExpandMore />}
        </ListItemButtonStyle>
        <Collapse in={menuItemOpens.get('user')} timeout="auto" unmountOnExit>
          <List component="div" disablePadding>
            <ListItemButtonStyle onClick={handleLogout}>
              <ListItemText primary="ログアウト" />
            </ListItemButtonStyle>
          </List>
        </Collapse>
      </ListItemStyle>
    </>
  );
};

class SideMenuClass implements ISideMenu {
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
    return <SideMenu />;
  }
}
export default SideMenuClass;
