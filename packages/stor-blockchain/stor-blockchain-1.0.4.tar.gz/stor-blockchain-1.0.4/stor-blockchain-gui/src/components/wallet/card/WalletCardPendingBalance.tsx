import React from 'react';
import { Trans } from '@lingui/macro';
import FarmCard from '../../farm/card/FarmCard';
import useWallet from '../../../hooks/useWallet';
import useCurrencyCode from '../../../hooks/useCurrencyCode';
import { storoshi_to_stor_string } from '../../../util/stor';

type Props = {
  wallet_id: number;
};

export default function WalletCardPendingBalance(props: Props) {
  const { wallet_id } = props;

  const { wallet, loading } = useWallet(wallet_id);
  const currencyCode = useCurrencyCode();

  const value = wallet?.wallet_balance?.balance_pending;

  return (
    <FarmCard
      loading={loading}
      valueColor="secondary"
      title={<Trans>Pending Balance</Trans>}
      tooltip={
        <Trans>
          This is the sum of the incoming and outgoing pending transactions (not
          yet included into the blockchain). This does not include farming
          rewards.
        </Trans>
      }
      value={
        <span>
          {storoshi_to_stor_string(value)} {currencyCode}
        </span>
      }
    />
  );
}
