import { createContext, useContext } from 'react';

import { ISideMenu } from '@/common/components/ISideMenu';
import { EMPTY, Empty } from '@/common/config/consts';

const SideMenuContext = createContext<ISideMenu | Empty>(EMPTY);

export const SideMenuProvider = SideMenuContext.Provider;
// export const useSideMenu = () => useContext(SideMenuContext);
export const useSideMenu = () => {
  const context = useContext(SideMenuContext);
  if (context === EMPTY) {
    throw new Error('useSideMenu must be used within a SideMenuProvider');
  }
  return context;
};
