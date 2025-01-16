import { IPageLinkType } from '@/common/config/types';

/**
 * カテゴリ
 */
export const CATEGORIES = {
  MENU: 'メニュー',
  MASTER: 'マスタ管理',
} as const;

export type CategoryType = (typeof CATEGORIES)[keyof typeof CATEGORIES];

/**
 * ページ
 */
export const PAGES = {
  MENU: 'メニュー',
  USER_REFERENCE: 'ユーザー照会',
} as const;

export type PageNameType = (typeof PAGES)[keyof typeof PAGES];

/**
 * ページリンク
 */
export const PAGE_LINKS: IPageLinkType = {
  // メニュー
  MENU: '/menu',
  // マスタ管理 > ユーザー照会
  USER_MASTER_REFERENCE: '/master/UserReference',
} as const;

export type PageLinkType = (typeof PAGE_LINKS)[keyof typeof PAGE_LINKS];

// export const PAGES = {
//   USER_MASTER_REFERENCE: {
//     subMenu: CATEGORIES.MASTER,
//     page: PAGES.USER_REFERENCE,
//     link: PAGE_LINK.USER_MASTER_REFERENCE,
// } as const;
