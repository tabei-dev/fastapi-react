import { JSX } from 'react';

/**
 * サイドメニュー情報インターフェース
 */
export interface ISideMenu {
  /**
   * ホームページリンクを取得します。
   * @returns {string} ホームページリンク
   */
  getHopePageLink(): string;

  /**
   * サイドメニューの子ノードを取得します。
   * @returns {JSX.Element} JSX.Element
   */
  getSiderMenuChildren(): JSX.Element;
}
