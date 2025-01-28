/**
 * サイドメニュー モジュールコンポーネント
 * Copyright (C) ITS Corporation. All Rights Reserved.
 */
import { JSX } from 'react';
import { Link } from 'react-router-dom';

import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import { Drawer, Box, AppBar, Toolbar, Card, CardMedia, IconButton, List } from '@mui/material';

import { useSelectedPage } from '@/shared/contexts/pageContext';
import { useSideMenu } from '@/shared/contexts/sideMenuContext';

// eslint-disable-next-line react-refresh/only-export-components
export const DRAWER_WIDTH = 250 as const;

type Props = {
  sideMenuOpen: boolean;
  setSideMenuOpen: React.Dispatch<React.SetStateAction<boolean>>;
};

/**
 * サイドメニュー
 * @param sideMenuOpen サイドメニュー開閉フラグ
 * @param setSideMenuOpen サイドメニュー開閉フラグ設定用関数
 * @returns {JSX.Element} JSX.Element
 */
const SideMenu = ({ sideMenuOpen, setSideMenuOpen }: Props): JSX.Element => {
  const sideMenu = useSideMenu();
  const selectedPage = useSelectedPage();

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
                <Link data-testid="linkMainMenu" to={sideMenu.getHopePageLink()}>
                  <Card sx={{ boxShadow: 'none', pt: 2, mb: 2 }}>
                    <CardMedia
                      sx={{ display: 'block', width: 150, ml: 1 }}
                      component="img"
                      image="/assets/images/logo_s.png"
                    />
                  </Card>
                </Link>
                <Box sx={{ ml: 'auto' }}>
                  {selectedPage.pageName && (
                    <IconButton onClick={() => setSideMenuOpen(false)}>
                      <ChevronLeftIcon />
                    </IconButton>
                  )}
                </Box>
              </Toolbar>
            </AppBar>
          </Box>
        }
      >
        {sideMenu.getSiderMenuChildren()}
      </List>
    </Drawer>
  );
};
export default SideMenu;
